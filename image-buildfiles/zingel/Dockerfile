FROM ubuntu:16.04

MAINTAINER adriansteffan "adrian.steffan@hotmail.de"

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

COPY ./requirements.txt /home/zingel/requirements.txt

WORKDIR /home/zingel

COPY . /home/zingel

RUN pip install -r requirements.txt
RUN pip install -U numpy


CMD python test_.py -i data -o out/zingel
