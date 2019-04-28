FROM ubuntu:16.04

MAINTAINER adriansteffan "adrian.steffan@hotmail.de"

RUN apt-get update -y

WORKDIR /home/emperor

COPY . /home/emperor

CMD /home/emperor/scripts/clickbait_regression.sh -i data -o out/emperor
