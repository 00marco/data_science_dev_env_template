# Base image
FROM python:3.9

# Updating repository sources
RUN apt-get update

# Copying source code to container
COPY . src

WORKDIR /src

# pip install dependencies
RUN pip install -r requirements.txt

