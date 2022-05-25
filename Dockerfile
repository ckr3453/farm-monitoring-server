FROM ubuntu:20.04

LABEL MAINTAINER myeonggil

# ADD nginx.tar.gz /


RUN apt-get update -y && \
        apt-get install -y build-essential zlib1g-dev \
        libncurses5-dev libgdbm-dev libnss3-dev vim \
        libssl-dev libreadline-dev libffi-dev curl \
        checkinstall libsqlite3-dev wget libbz2-dev \
        git


RUN ln -snf /usr/share/zoneinfo/Asia/Seoul /etc/localtime

RUN apt-get install -y nginx && \
        apt-get install -y redis



# nginx의 기본 설정을 삭제하고 앱에서 설정한 파일을 복사
# RUN cp /nginx.conf /etc/nginx/conf.d


RUN wget https://www.python.org/ftp/python/3.9.9/Python-3.9.9.tgz && \
        tar -xf Python-3.9.9.tgz

RUN cd Python-3.9.9 && \
        ./configure --enable-optimizations && \
        make -j 12 && \
        make altinstall

RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
        python3.9 get-pip.py

RUN ln -s /usr/local/bin/python3.9 /usr/bin/python

ENV PYTHONPATH /usr/bin/python

ENV LANG ko_KR.UTF-8
ENV LANGUAGE ko_KR.UTF-8

WORKDIR /home/ec2-user

