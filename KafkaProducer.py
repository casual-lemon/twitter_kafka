#!/usr.bin.python
from kafka import KafkaProducer

import json


class KafkaTestProducer:

    def __init__(self):
        bootstrap_servers = ['localhost:9092']
        self.topic_name = 'kafka_tweets'
        self.producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
        print(self.producer.bootstrap_connected())

    def get_twitter_stream(self, twitter_stream):
        for line in twitter_stream:
            try:
                if line.get(id) is not None:
                    key = line.get('id')
                    value = line.get('text')
                    key_bytes = bytes(str.encode(key))
                    value_bytes = bytes(str.encode(value))
                    record_metadata = self.producer.send(self.topic_name, key=key_bytes, value=value_bytes)
                    print("Message sent to kafka consumer")
                    print(record_metadata.get('topic'))
                    print(record_metadata.get('partition'))
                    print(record_metadata.get('offset'))
                    # self.producer.flush()
            except Exception as ex:
                print("Error sending message to kafka.", str(ex))
        self.producer.close()


if __name__ == "__main__":
    KafkaTestProducer()
