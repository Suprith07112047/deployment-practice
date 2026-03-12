#!/bin/bash
set -e

# Ensure Docker service is running
#sudo systemctl start docker

# Optional: wait a moment for Docker to be ready
#sleep 5

# pull the docker image from docker hub
docker pull suprithreddy789/deployment-practice:latest

# stop and remove any old container
docker stop deployment-practice || true
docker rm deployment-practice || true

# run the docker image as a container
docker run -d -p 8080:8080 --name deployment-practice suprithreddy789/deployment-practice:latest
