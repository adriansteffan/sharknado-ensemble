FROM ubuntu:16.04

MAINTAINER adriansteffan "adrian.steffan@hotmail.de"

RUN add-apt-repository ppa:deadsnakes/ppa

RUN apt-get update -y && \
    apt-get install -y python3.4 python3-pip
	

COPY ./requirements.txt /home/houndshark/requirements.txt

WORKDIR /home/houndshark

COPY . /home/houndshark

RUN pip3 install --upgrade pip 

RUN pip3 install -r requirements.txt


CMD python3.4 2ndModel/clickBait_classification_v2.py data out/houndshark