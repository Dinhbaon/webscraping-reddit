terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
    }
  }

}

provider "aws" {
  region  = "us-east-2" 
  profile = "terraform"
  
}

provider "aws" {
  alias = "acm"
  region = "us-east-1"
  profile = "terraform"
}

data "aws_instance" "existing_instance" {
  filter {
    name = "network-interface.addresses.association.public-dns-name"
    values = [aws_eip.default_eip.public_dns] 
  }

  depends_on = [aws_autoscaling_group.default_asg, aws_network_interface.default_eni, aws_eip.default_eip]
}

module "oidc_github" {
  source  = "unfunco/oidc-github/aws"
  version = "1.7.1"
  attach_admin_policy = true
  github_repositories = [
    "Dinhbaon/webscraping-reddit"
  ]
}

resource "aws_ecr_repository" "Spring-boot-backend" {
  name = "webscrapingcollegeresults"
  image_tag_mutability = "MUTABLE"
}

resource "aws_ecr_lifecycle_policy" "lifecycle_policy" {
  repository = aws_ecr_repository.Spring-boot-backend.name

  policy = <<EOF
{
    "rules": [
        {
            "rulePriority": 1,
            "description": "Keep last image",
            "selection": {
                "tagStatus": "any",
                "countType": "imageCountMoreThan",
                "countNumber": 1
            },
            "action": {
                "type": "expire"
            }
        }
    ]
}
EOF
}
resource "aws_vpc" "main" {
 cidr_block = "10.0.0.0/16"
 enable_dns_hostnames = true
 
 tags = {
   Name = "Project VPC"
 }
}

resource "aws_cloudfront_distribution" "ec2_distribution" {
  is_ipv6_enabled     = true
  enabled             = true
    viewer_certificate {
    acm_certificate_arn = "${aws_acm_certificate.cert.arn}"
  }

  origin {
    domain_name              = aws_network_interface.default_eni.private_dns_name
    origin_id                = "us-east-2"
  }

    default_cache_behavior {
    allowed_methods  = ["DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT"]
    cached_methods   = ["GET", "HEAD"]
    target_origin_id = data.aws_instance.existing_instance.id
    viewer_protocol_policy = "allow-all"
    forwarded_values {
      query_string = false

      cookies {
        forward = "none"
      }
    }
  }
    restrictions {
      geo_restriction {
        restriction_type = "whitelist"
      }
    }
}


resource "aws_subnet" "public" {
  vpc_id = aws_vpc.main.id
  cidr_block = "10.0.0.0/17"
}

resource "aws_subnet" "private" {
  vpc_id = aws_vpc.main.id
  cidr_block = "10.0.128.0/17"
}

resource "aws_route_table" "default_route_table" {
  vpc_id = aws_vpc.main.id
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.default_igw.id
  }

}

resource "aws_route_table_association" "route_table_association" {
  subnet_id      = aws_subnet.public.id
  route_table_id = aws_route_table.default_route_table.id
}

resource "aws_internet_gateway" "default_igw" {
  vpc_id = aws_vpc.main.id
}

resource "aws_network_interface" "default_eni" {
  subnet_id = aws_subnet.public.id
  security_groups = [aws_security_group.default_sg.id]
}

resource "aws_eip" "default_eip" {
  depends_on                = [aws_internet_gateway.default_igw]
}

resource "aws_eip_association" "eip_assoc" {
  allocation_id = aws_eip.default_eip.id
  network_interface_id = aws_network_interface.default_eni.id
}

resource "aws_acm_certificate" "cert" {
  provider = "aws.acm"
  domain_name       = aws_eip.default_eip.public_dns
  validation_method = "DNS"

  lifecycle {
    create_before_destroy = true
  }


  depends_on = [data.aws_instance.existing_instance]
}

resource "aws_route53_zone" "public_zone" {
  provider = "aws.acm"
  name = aws_eip.default_eip.public_dns
  depends_on = [aws_eip.default_eip]
}

resource "aws_route53_record" "cert_dns" {
  provider = "aws.acm"
  allow_overwrite = true
  name =  tolist(aws_acm_certificate.cert.domain_validation_options)[0].resource_record_name
  records = [tolist(aws_acm_certificate.cert.domain_validation_options)[0].resource_record_value]
  type = tolist(aws_acm_certificate.cert.domain_validation_options)[0].resource_record_type
  zone_id = aws_route53_zone.public_zone.zone_id
  ttl = 300
}

resource "aws_acm_certificate_validation" "certicate_validation" {
  provider = "aws.acm"
  certificate_arn  = aws_acm_certificate.cert.arn
  validation_record_fqdns = [aws_route53_record.cert_dns.fqdn]

  timeouts {
    create = "2h"
  }

}

resource "aws_security_group" "default_sg" {
  vpc_id      = aws_vpc.main.id
  ingress {
    from_port   = "80"
    to_port     = "80"
    protocol    = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  ingress {
    from_port = "8080"
    to_port = "8080"
    protocol = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  ingress {
    from_port = "22"
    to_port = "22"
    protocol = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }
}


resource "aws_ecs_cluster" "default_cluster" {
  name = "RedditCollegeResultsCluster"
}

resource "aws_ecs_service" "default_service" {
  name = "RedditCollegeResultsService"
  task_definition = "${aws_ecs_task_definition.default_backend_task.family}:${aws_ecs_task_definition.default_backend_task.revision}"
  cluster = aws_ecs_cluster.default_cluster.id
  force_new_deployment = true
  desired_count = 1
  deployment_minimum_healthy_percent = 0
  deployment_maximum_percent         = 100

  depends_on = [aws_route_table.default_route_table] 
}

resource "aws_ecs_task_definition" "default_backend_task" {
  family = "RedditCollegeResultsBackend"
  execution_role_arn = "arn:aws:iam::203615242357:role/ecsTaskExecutionRole" 
  cpu = 1024
  memory = 800
  requires_compatibilities = ["EC2"]
  container_definitions = jsonencode([{
            "name": "Backend",
            "image": "203615242357.dkr.ecr.us-east-2.amazonaws.com/webscrapingcollegeresults:latest",
            "cpu": 0,
            "memory": 800,
            "memoryReservation": 800,
            "portMappings": [
                {
                    "name": "backend-80-tcp",
                    "containerPort": 8080,
                    "hostPort": 8080,
                    "protocol": "tcp",
                    "appProtocol": "http"
                }
            ],
            "essential": true,
            "environment": [],
            "environmentFiles": [],
            "mountPoints": [],
            "volumesFrom": [],
            "ulimits": [],
            "logConfiguration": {
                "logDriver": "awslogs",
                "options": {
                    "awslogs-create-group": "true",
                    "awslogs-group": "/ecs/RedditCollegeResultsBackend",
                    "awslogs-region": "us-east-2",
                    "awslogs-stream-prefix": "ecs"
                },
                "secretOptions": []
            },
            "systemControls": []
        }])
    network_mode = "host"
}

resource "aws_iam_instance_profile" "ec2_profile" {
  name = "backend_ec2_profile"
  role = "ecsInstanceRole"
}

resource "aws_iam_role" "default_ec2_role" {
  name = "default_ec2_role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17", 
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Sid = ""
        Principal = {
          Service = "ec2.amazonaws.com"
        }
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "default_ec2_role_attachment" {
  role       = aws_iam_role.default_ec2_role.name
  policy_arn = data.aws_iam_policy.AmazonEC2ContainerServiceforEC2Role.arn
}

data "aws_iam_policy" "AmazonEC2ContainerServiceforEC2Role" {
  arn = "arn:aws:iam::aws:policy/service-role/AmazonEC2ContainerServiceforEC2Role"
}

resource "aws_launch_template" "default_ec2" {
  name_prefix   = "default_ec2"
  image_id      = "ami-0d7a88a80216e41f0"
  instance_type = "t2.micro"
  user_data = filebase64("cluster.sh")
  

  iam_instance_profile {
    arn = aws_iam_instance_profile.ec2_profile.arn
  }
  network_interfaces {
    network_interface_id = aws_network_interface.default_eni.id
  }

  tag_specifications {
    resource_type = "instance"

    tags = {
      Name = "main"
    }
  }

  depends_on = [aws_ecs_cluster.default_cluster]
}

resource "aws_autoscaling_group" "default_asg" {
  min_size = 1 
  max_size = 2
  desired_capacity = 1
  availability_zones = ["us-east-2b"]
  launch_template {
    id      = aws_launch_template.default_ec2.id
    version = "$Latest"
  }
}

resource "aws_ecs_capacity_provider" "default_capacity_provider" {
  name = "default_capacity_provider"

  auto_scaling_group_provider {
    auto_scaling_group_arn         = aws_autoscaling_group.default_asg.arn

    managed_scaling {
      maximum_scaling_step_size = 2
      minimum_scaling_step_size = 1
      status                    = "ENABLED"
      target_capacity           = 1
    }
  }


}

resource "aws_ecs_cluster_capacity_providers" "example" {
  cluster_name = aws_ecs_cluster.default_cluster.name

  capacity_providers = [aws_ecs_capacity_provider.default_capacity_provider.name]

  default_capacity_provider_strategy {
    base = 1
    weight = 100
    capacity_provider = aws_ecs_capacity_provider.default_capacity_provider.name
  }

}

