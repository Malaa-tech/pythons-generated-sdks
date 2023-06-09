FROM node:14

ENV GOPATH=/go
ENV PATH=$GOPATH/bin:/usr/local/go/bin:/root/.task/bin:$PATH

RUN apt-get update && \
    apt-get install -y curl default-jre && \
    curl -sL https://taskfile.dev/install.sh | sh && \
    npm install -g @openapitools/openapi-generator-cli     