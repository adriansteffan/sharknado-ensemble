FROM ubuntu:16.04

MAINTAINER adriansteffan "adrian.steffan@hotmail.de"

RUN apt-get update -y

WORKDIR /home/pineapplefish

COPY . /home/pineapplefish

CMD cd anaconda ;./bin/python ./clickbait_regression/ensemble_classifier.py -i ../data -o ../out/pineapplefish
