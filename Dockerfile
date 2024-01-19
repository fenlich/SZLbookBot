FROM python:3.10-slim-buster
LABEL authors="bloodrain"

WORKDIR /bookBot

COPY /requirements.txt requirements.txt
COPY /szl_bot.py szl_bot.py
COPY /config.py config.py
COPY /books.csv books.csv

RUN pip3 install -r requirements.txt
RUN pip3 install python-telegram-bot[job-queue]


CMD ["python3", "-m" , "szl_bot", "run"]
