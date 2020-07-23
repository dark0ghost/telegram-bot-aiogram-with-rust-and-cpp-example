FROM DEBIAN:10
FROM PYTHON:3.8
FROM rust:1.31


RUN mkdir /usr/src/app
WORKDIR /usr/src/app
ADD . /usr/src/app

RUN ca

RUN  apt-get install --no-install-recommends -y python3-distutils
RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .

RUN sh -ac 'cd /usr/src/app && python3 start_polling.py'