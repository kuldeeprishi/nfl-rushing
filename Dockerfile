FROM ubuntu:bionic

LABEL maintainer="kuldeep@hotstar.com"
LABEL Name theScore
LABEL Version 1.0.0
LABEL RUN /usr/bin/docker -d IMAGE

RUN apt-get update -y && \
    apt-get install -y python3-pip locales

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app


RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

ENTRYPOINT ["scripts/entry.sh"]
