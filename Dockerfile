FROM python:3

RUN groupadd --gid 1000 user \
    && useradd --uid 1000 --gid user --shell /bin/bash --create-home user

USER user

ENV PYTHONUNBUFFERED=1

WORKDIR /home/user/task
COPY requirements.txt /home/user/task/

RUN pip install -r requirements.txt
COPY . /home/user/task