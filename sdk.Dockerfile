FROM golang:1.17

ENV GOPATH=/go
ENV PATH=$GOPATH/bin:/usr/local/go/bin:/root/.task/bin:$PATH

RUN apt-get update && \
    apt-get install -y curl && \
    curl -sL https://taskfile.dev/install.sh | sh && \
    curl -o /usr/local/bin/openapi-generator https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/5.3.0/openapi-generator-cli-5.3.0.jar && \
    chmod +x /usr/local/bin/openapi-generator

WORKDIR /
