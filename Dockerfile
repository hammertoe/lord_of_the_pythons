FROM python:3.7-slim

WORKDIR /app

ADD . /app

ENTRYPOINT ["python"]

CMD ["/app/lord_of_the_pythons.py"]