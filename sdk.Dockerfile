FROM node:14

ENV GOPATH=/go
ENV PATH=$GOPATH/bin:/usr/local/go/bin:/root/.task/bin:$PATH

RUN apt-get update && \
    apt-get install -y curl && \
    curl -sL https://taskfile.dev/install.sh | sh && \
    npm install @openapitools/openapi-generator-cli -g

WORKDIR /
