# docker build -t 192.168.122.15:30500/python:3-alpine  .
FROM python:3-alpine

RUN apk add curl && \
    pip install flask pytest

EXPOSE 4000

CMD python app.py
