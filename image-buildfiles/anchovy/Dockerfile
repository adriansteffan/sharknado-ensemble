FROM ubuntu:16.04

MAINTAINER adriansteffan "adrian.steffan@hotmail.de"

RUN apt-get update -y && \
    apt-get install -y python3 python3-pip

COPY ./requirements.txt /home/anchovy/requirements.txt

WORKDIR /home/anchovy

COPY . /home/anchovy

RUN pip3 install --upgrade pip 

RUN pip3 install -r requirements.txt

CMD python3 anchovy/test.py -i data -o out/anchovy

