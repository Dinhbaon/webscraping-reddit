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


module "oidc_github" {
  source  = "unfunco/oidc-github/aws"
  version = "1.7.1"

  github_repositories = [
    "Dinhbaon/webscraping-reddit"
  ]
}

resource "aws_ecr_repository" "Spring-boot-backend" {
  name = "webscrapingcollegeresults"
  image_tag_mutability = "MUTABLE"
}