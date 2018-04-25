FROM python:3.4

ENV PYTHONUNBUFFERED 1

#create containers mountpoints
RUN mkdir /code
RUN mkdir /config
WORKDIR /code

ADD ./docker/* /config/
RUN chmod a+x /config/docker_entrypoint.py
RUN pip install -r /config/requirements.txt