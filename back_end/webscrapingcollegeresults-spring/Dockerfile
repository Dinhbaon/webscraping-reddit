FROM amazoncorretto:17-alpine-jdk
MAINTAINER baeldung.com
RUN mkdir -p $HOME/.postgresql/ && \
    wget -O $HOME/.postgresql/root.crt 'https://cockroachlabs.cloud/clusters/1385aaf7-3b26-4af7-aaf3-12ebc865bdf3/cert'
RUN apk update
RUN apk upgrade --available
RUN apk add --upgrade --no-cache ca-certificates && update-ca-certificates
COPY target/WebScrapingCollegeResults-0.0.1-SNAPSHOT.jar WebScrapingCollegeResults-0.0.1-SNAPSHOT.jar
ENTRYPOINT ["java","-jar","/WebScrapingCollegeResults-0.0.1-SNAPSHOT.jar"]