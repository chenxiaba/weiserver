#Create a new tornado server
FROM python:2.7
MAINTAINER chenxiaba <chenxiaba@gmail.com>
EXPOSE 8888

RUN apt-get update && apt-get install -y mysql-client
#RUN  apt-get install -y mysql-client

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install -r requirements.txt

COPY . /usr/src/app

CMD python weiserver.py