#!/usr.bin.python
from kafka import KafkaProducer

import json


class KafkaTestProducer:
    bootstrap_servers = ['localhost:9092']
    topic_name = 'bigdata_tweets'
    producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
    ack = producer.send(topic_name, json.dumps([]).encode())
    metadata = ack.get()
    print(metadata.topic)
    print(metadata.partition)
    print(metadata.offset)


if __name__ == "__main__":
    KafkaTestProducer()
