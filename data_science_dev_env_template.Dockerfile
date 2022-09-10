# Base image
FROM python:3.7.12

# Updating repository sources
RUN apt-get update

# Copying source code to container
COPY . src

# pip install dependencies
WORKDIR /src

RUN pip install -r requirements.txt

# Exposing ports
EXPOSE 8887
EXPOSE 443
EXPOSE 993
EXPOSE 143
EXPOSE 25
EXPOSE 587

# Running jupyter notebook
CMD ["python", "main.py"]
