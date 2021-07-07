FROM openjdk:16-jdk-alpine

RUN apk add python3 py3-pip python3-dev gcc

RUN ln -s /usr/bin/python3 /usr/bin/python & \
    ln -s /usr/bin/pip3 /usr/bin/pip