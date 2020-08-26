FROM python:3.7-alpine3.9

#build args, for custom python libs
ARG WORKSPACE=stickone
ARG BRANCH_UTIL_LIB=master
ARG BRANCH_UTIL_MODEL=master

RUN apk update \
    && apk add --no-cache --virtual .build-deps gcc libc-dev \
    #some no required but util dependencies
    #&& apk add --no-cache --virtual .build-deps gcc libc-dev libxslt-dev \
    #&& apk add --no-cache libxslt \
    #&& apk add --update build-base git make \
    #&& apk add libffi-dev openssh tzdata mysql-dev \
    && pip install --upgrade pip \
    && pip install gunicorn==19.9.0

WORKDIR /app-run
COPY . /app-run

#RUN pip install --no-cache-dir -r /app-run/requirements.txt
RUN pip install -r /app-run/requirements.txt

# if you need install custom python libs, don't forget put your public ssh key to ./ssh/pkey to connect your repo
#RUN ash /app-run/sh/install_libs.sh

RUN apk del .build-deps


ENTRYPOINT gunicorn --conf /app-run/server_conf.py server:app --reload
