# syntax=docker/dockerfile:1
FROM python:3.7-alpine
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY tcmgcli.py tcmgcli.py
ENTRYPOINT ["python3", "./tcmgcli.py"]
