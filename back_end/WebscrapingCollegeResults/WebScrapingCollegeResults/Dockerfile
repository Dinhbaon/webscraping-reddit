FROM amazoncorretto:17-alpine-jdk
MAINTAINER baeldung.com
COPY ./root.crt /root/.postgresql/root.crt
RUN apk update
RUN apk upgrade --available
RUN apk add --upgrade --no-cache ca-certificates && update-ca-certificates
COPY target/WebScrapingCollegeResults-0.0.1-SNAPSHOT.jar WebScrapingCollegeResults-0.0.1-SNAPSHOT.jar
ENTRYPOINT ["java","-jar","/WebScrapingCollegeResults-0.0.1-SNAPSHOT.jar"]