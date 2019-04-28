FROM ubuntu:16.04

MAINTAINER adriansteffan "adrian.steffan@hotmail.de"

RUN apt-get update -y && \
    apt-get install -y python3 python3-pip

COPY ./requirements.txt /home/pike/requirements.txt

WORKDIR /home/pike

COPY . /home/pike

RUN pip3 install --upgrade pip 

RUN pip3 install -r requirements.txt

CMD python3 clickbait/runmodel.py clickbait/clfRF_regressor_nestimators400_maxdepth_20_60features_180.pkl data out/pike