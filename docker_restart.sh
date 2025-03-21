#!/bin/bash

CONTAINER_NAME="selenium_chrome"

docker stop $CONTAINER_NAME
docker rm -f $CONTAINER_NAME

docker run -d -p 4444:4444 -p 7900:7900 --shm-size="2g" --name=$CONTAINER_NAME selenium/standalone-chrome:latest
