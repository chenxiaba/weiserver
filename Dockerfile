#Create a new tornado server
FROM python:2.7
MAINTAINER chenxiaba <chenxiaba@gmail.com>
EXPOSE 8888

RUN apt-get update && apt-get install -y mysql-client

#copy code
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

#update pip
RUN pip install --upgrade pip

COPY requirements.txt /usr/src/app/
RUN pip install --trusted-host pypi.douban.com -i http://pypi.douban.com/simple -r requirements.txt

COPY . /usr/src/app

CMD python weiserver.py
