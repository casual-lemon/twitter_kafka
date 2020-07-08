#!/usr.bin.python
from kafka import KafkaConsumer


class KafkaTestConsumer:
    bootstrap_servers = ['localhost:9092']
    topic_name = 'bigdata_tweets'

    producer = KafkaConsumer(bootstrap_servers=bootstrap_servers)

    ack = producer.send(topic_name)
    metadata = ack.get()
    print(metadata.topic)
    print(metadata.partition)
    print(metadata.offset)


if __name__ == "__main__":
    KafkaTestConsumer()
