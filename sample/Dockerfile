# docker build -t flask:v1 .
FROM 192.168.122.15:30500/python:3-alpine

WORKDIR /work

COPY app.py test_1.py /work/

EXPOSE 8080

CMD python app.py
