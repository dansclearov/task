FROM python:3

RUN groupadd --gid 1000 user \
    && useradd --uid 1000 --gid user --shell /bin/bash

ENV PYTHONUNBUFFERED=1

WORKDIR /task
COPY requirements.txt /task/

RUN pip install -r requirements.txt
COPY . /task