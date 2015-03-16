import tweepy
from lyrics import Scraper
from utils import ex
s = Scraper()


class Twitter:

    config = {}
    try:
        execfile("keys.conf", config)
    except IOError:
        print "Please specify your Twitter keys credentials as \"keys.conf\" file."
        ex()
    
    def __init__(self):
        self.api = ""
        self.auth()

    def auth(self):
        auth = tweepy.OAuthHandler(self.config['consumer_key'], self.config['consumer_secret'])
        auth.set_access_token(self.config['access_token'], self.config['access_secret'])
        self.api = tweepy.API(auth)
        return self.api

    def update(self, status):
        try:
            self.api.update_status(status)
        except Exception as e:
            s.error(e)
            self.api.update_status(status)
