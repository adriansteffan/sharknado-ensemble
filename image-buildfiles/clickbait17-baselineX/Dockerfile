FROM ubuntu:16.04

MAINTAINER adriansteffan "adrian.steffan@hotmail.de"

RUN apt-get update -y && \
    apt-get install -y python3 python3-pip

COPY ./requirements.txt /home/clickbait17-baseline/requirements.txt

WORKDIR /home/clickbait17-baseline

COPY . /home/clickbait17-baseline

RUN pip3 install --upgrade pip 

RUN pip3 install -r requirements.txt

CMD cd /home/clickbait17-baseline/clickbait-detection/src-py; python3 /home/clickbait17-baseline/clickbait-detection/src-py/predict.py /home/clickbait17-baseline/data/instances.jsonl /home/clickbait17-baseline/out/clickbait17-baseline/results.jsonl
