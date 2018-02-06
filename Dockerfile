FROM python:3.5.2-slim

WORKDIR /usr

RUN apt-get update && \
    apt-get install -y \
      unzip \
      wget \
      git \
      gcc \
      g++ \
      make

RUN wget https://github.com/edenhill/librdkafka/archive/debian/0.9.1-1.zip && \
    unzip 0.9.1-1.zip && \
    rm 0.9.1-1.zip && \
    ls && \
    cd librdkafka-debian-0.9.1-1 && \
    ./configure && \
    make && \
    make install && \
    cd ..



WORKDIR /app

ENV PYTHONPATH /app
ENV PYTHONUNBUFFERED true

ADD . /app

RUN pip install confluent-kafka

# for AvroProducer or AvroConsumer
RUN pip install confluent-kafka[avro]

EXPOSE 5000
ENTRYPOINT while :; do read; done
