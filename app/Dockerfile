# syntax=docker/dockerfile:1

# set base image
FROM tensorflow/tensorflow:latest-gpu

# set the working directory in the container
WORKDIR /code

# set environment variables used by the flask command.
ENV FLASK_APP=server.py
ENV FLASK_RUN_HOST=0.0.0.0

# install dependencies & clear cache
RUN apt-get update && apt-get install -y \
    gcc musl-dev linux-headers-generic \
    && rm -rf /var/lib/apt/lists/*

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# add metadata to the image to describe that the container is listening on port 5000
EXPOSE 5000

# copy the content of the local src directory to the working directory
COPY src/ .

# command to run on container start
CMD [ "flask", "run" ]