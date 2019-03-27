FROM python:3

MAINTAINER andoniaf

RUN mkdir -p /pyemtbot/logs

WORKDIR /pyemtbot

COPY requirements.txt /pyemtbot

RUN pip install -r requirements.txt

COPY . /pyemtbot

ENTRYPOINT [ "python", "./bot.py" ]
