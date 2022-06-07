#syntax=docker/dockerfile:1
FROM python:3.8-slim-buster

WORKDIR /action
COPY . .

ENTRYPOINT ["/action/entrypoint.sh"]
