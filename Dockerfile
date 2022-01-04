# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements requirements
COPY translator.py translator.py
RUN pip3 install -r requirements

EXPOSE 8080

CMD [ "python3", "translator.py"]
