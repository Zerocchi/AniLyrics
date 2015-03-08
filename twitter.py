import tweepy
from lyrics import Scraper
s = Scraper()

class Twitter:

    # Go to dev.twitter.com and make your own app. Get the following keys.
    consumer_key = ""
    consumer_secret = ""
    access_token = ""
    access_secret = ""
    
    def __init__(self):
        self.api = ""
        self.auth()

    def auth(self):
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_secret)
        self.api = tweepy.API(auth)
        return self.api

    def update(self, status):
        try:
            self.api.update_status(status)
        except Exception as e:
            s.error(e)
            self.api.update_status(status)
