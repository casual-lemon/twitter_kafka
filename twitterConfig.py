#!/usr.bin.python
""" Twitter connection setup"""
import json


class TwitterConfig:

    def __init__(self):
        try:
            with open('config.json', 'r') as json_data_file:
                config = json.load(json_data_file)
                self.token_key = config['token_key']
                self.token_secret = config['token_secret']
                self.consumer_key = config['consumer_key']
                self.consumer_secret = config['consumer_secret']
        finally:
            json_data_file.close()


if __name__ == "__main__":
    TwitterConfig()
