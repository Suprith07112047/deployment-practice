#!/bin/bash
set -e
#pull the docker image from docker hub
docker pull suprithreddy789/deployment-practice

#run the docker image as a container
docker run -d -p 8080:8080 suprithreddy789/deployment-practice
