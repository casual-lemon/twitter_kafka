#!/usr.bin.python
from kafka import KafkaConsumer


class KafkaTestConsumer:
    bootstrap_servers = ['localhost:2888']
    topic_name = 'kafka_tweets'

    def consume_messages(self):
        try:
            kafka_consumer = KafkaConsumer(self.topic_name, bootstrap_servers=self.bootstrap_servers)
            print(kafka_consumer.bootstrap_connected())
            if kafka_consumer is not None:
                for message in kafka_consumer:
                    # message value and key are raw bytes -- decode if necessary!
                    # e.g., for unicode: `message.value.decode('utf-8')`
                    print(message)
                    # print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                    #                                      message.offset, message.key,
                    #                                      message.value))
        except Exception as ex:
            print("Failure in consume messages", ex)


if __name__ == "__main__":
    kafka = KafkaTestConsumer()
    kafka.consume_messages()
