FROM ubuntu:16.04

MAINTAINER adriansteffan "adrian.steffan@hotmail.de"

RUN apt-get update -y && \
    apt-get install -y python3 python3-pip

COPY ./requirements.txt /home/whitebait/requirements.txt

WORKDIR /home/whitebait

COPY . /home/whitebait

RUN pip3 install --upgrade pip 

RUN pip3 install -r requirements.txt

CMD python3 SCRIPT -i data -o out/whitebait

CMD ./myClassifier.py -i data -o out/whitebait