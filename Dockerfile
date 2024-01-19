FROM python:3.6

RUN apt-get -y update
RUN apt-get -y install python
RUN apt-get -y install gunicorn

RUN pip install -r requirements.txt

COPY . /opt/src