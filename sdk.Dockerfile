FROM golang:1.17

ENV GOPATH=/go
ENV PATH=$GOPATH/bin:/usr/local/go/bin:$PATH

RUN apt-get update && \
    apt-get install -y python3-pip && \
    curl -sL https://taskfile.dev/install.sh | sh

WORKDIR /