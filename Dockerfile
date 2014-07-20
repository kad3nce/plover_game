FROM ubuntu:14.04
MAINTAINER kad3nce

RUN DEBIAN_FRONTEND=noninteractive apt-get update --fix-missing
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y python3 python3-pip

RUN mkdir /app
WORKDIR /app

EXPOSE 8080
CMD ["python3", "server.py"]

ADD requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt

ADD . /app
