FROM winamd64/python:latest

RUN mkdir /app

WORKDIR /app

RUN pip install flask waitress

ADD app.py .

CMD python /app/app.py
