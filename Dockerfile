FROM ubuntu

RUN apt-get -y update
RUN apt-get -y install software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get -y install python3.7
RUN apt-get -y install python3-pip
RUN apt-get -y install gunicorn

COPY . /opt/src

RUN pip install -r /opt/src/requirements.txt

CMD [ "sh", "/opt/src/gunicorn_start.sh" ]