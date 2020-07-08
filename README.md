# Streaming Twitter Data & Kafka

Login and create credentials for Twitter Developer

https://developer.twitter.com/en

Helm install: 

`helm install kafka --set persistence.enabled=false --set zookeeper.persistence.enabled=false bitnami/kafka`

Run twitterConfig.py first to save off connection info

Run Tweets.py 

Run KafkaProducer.py

Run KafkaConsumer.py













