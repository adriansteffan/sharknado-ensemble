FROM ubuntu:16.04

MAINTAINER adriansteffan "adrian.steffan@hotmail.de"

RUN apt-get update -y && \
    apt-get install -y python3 python3-pip apturl apturl-common

COPY ./requirements.txt /home/albacore/requirements.txt

WORKDIR /home/albacore

COPY . /home/albacore

RUN pip3 install --upgrade pip 

RUN pip3 install -r requirements.txt

CMD python3 /home/albacore/omidvar/Tira/test.py data out/albacore

