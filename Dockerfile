FROM python:3.9-slim-buster

WORKDIR /application
COPY ./app /application/app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

CMD uvicon --host=0.0.0.0 --port 8080 app.main.app