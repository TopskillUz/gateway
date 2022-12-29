FROM python:3.10-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1




RUN mkdir /service
WORKDIR /service

COPY ./protos /service/protos/
COPY . /service/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN python -m grpc_tools.protoc -I protos --python_out=. --grpc_python_out=. protos/*.proto


ENTRYPOINT ["python", "main.py"]