FROM ubuntu:16.04

MAINTAINER adriansteffan "adrian.steffan@hotmail.de"

RUN apt-get update -y

WORKDIR /home/carpetshark

COPY . /home/carpetshark

CMD cd clickbait ; /home/carpetshark/anaconda3/bin/python /home/carpetshark/clickbait/predict.py ../data ../out/carpetshark