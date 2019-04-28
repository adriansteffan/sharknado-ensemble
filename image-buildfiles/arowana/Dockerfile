FROM ubuntu:16.04

MAINTAINER adriansteffan "adrian.steffan@hotmail.de"

RUN apt-get update -y && \
    apt-get install -y python python-pip

COPY ./requirements.txt /home/arowana/requirements.txt

WORKDIR /home/arowana

COPY . /home/arowana

RUN pip install --upgrade pip 

RUN pip install -r requirements.txt

RUN pip install -r requirements.txt
RUN pip install -U numpy

CMD cd clickbait ; python muti_clf.py -c ../data -o ../out/arowana

