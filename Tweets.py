#!/usr/bin/python3.8
""" Pulls twitter data via twitter API"""
import twitter

from twitterConfig import TwitterConfig


class Tweets:

    def __init__(self):
        config = TwitterConfig()
        self.twitter_api = twitter.Api(config.consumer_key,
                                       config.consumer_secret,
                                       config.token_key, config.token_secret)

    def getTweets(self):
        # user = self.twitter_api.GetUser(screen_name="realDonaldTrump")
        # tweets = self.twitter_api.GetUserTimeline(screen_name="realDonaldTrump")
        twitter_stream = self.twitter_api.GetStreamSample()
        for line in twitter_stream:
            print(line.get('id'))
            print(line.get('text'))


if __name__ == "__main__":
    tweet = Tweets()
    tweet.getTweets()
