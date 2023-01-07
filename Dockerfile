FROM python:3.10-slim-bullseye
#FROM gcr.io/google_appengine/python:latest

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /service
WORKDIR /service

COPY ./protos /service/protos/
COPY . /service/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

#RUN python -m grpc_tools.protoc -I protos --python_out=grpc_generated_files --grpc_python_out=grpc_generated_files protos/*.proto

HEALTHCHECK CMD curl --fail http://localhost:8080/ || exit 1
ENTRYPOINT ["python", "main.py"]