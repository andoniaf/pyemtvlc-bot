FROM python:3

RUN mkdir /pyemtbot

WORKDIR /pyemtbot

COPY requirements.txt /pyemtbot

RUN pip install -r requirements.txt

COPY . /pyemtbot

CMD [ "python", "./bot.py" ]
