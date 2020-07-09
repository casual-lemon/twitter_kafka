#!/usr.bin.python
from kafka import KafkaProducer


class KafkaTestProducer:

    def __init__(self):
        try:
            bootstrap_servers = ['localhost:2888']
            self.topic_name = 'kafka_tweets'
            self.producer = KafkaProducer(bootstrap_servers=['localhost:2888'])
            print(self.producer.bootstrap_connected())
        except Exception as ex:
            print("Error connecting to kafka.", str(ex))
            self.producer.close()

    def get_twitter_stream(self, twitter_stream):
        for line in twitter_stream:
            try:
                key = line.get('id')
                value = line.get('text')
                if key is not None and value is not None:
                    self.producer.send(self.topic_name, str(key).encode("utf-8"),value.encode("utf-8"))
                    print("Message sent to kafka consumer")
                    self.producer.flush()
            except Exception as ex:
                print("Error sending message to kafka.", str(ex))
        self.producer.close()


if __name__ == "__main__":
    KafkaTestProducer()
