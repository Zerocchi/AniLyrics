import tweepy
from lyrics import Scraper
s = Scraper()

class Twitter:

	# Go to dev.twitter.com and make your own app. Get the following keys.
<<<<<<< HEAD
	consumer_key = "8Gs7MNjwgmEeOEI0c3i3jfHzu"
	consumer_secret = "89IZ2rfjwy2Kef3D7b4C0e4z9M83YowQoXgCCxVIsX4sFTIBKs"
	access_token  = "2170046142-OHZ6OEEBKWxDmhBzOpYM2XW1g55riVr2j3R6wAg" 
	access_secret = "PrUQWZV6wIDjJ3aIya4mcvAcadDis2vS9xuiJgkuNuhCX"
=======
	consumer_key = ""
	consumer_secret = ""
	access_token  = "" 
	access_secret = ""
>>>>>>> 953a4210b46bb9cb23ac35aaddbf45e21bbf5bb2

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
<<<<<<< HEAD
		except Exception as e:
			s.error(e)
			self.api.update_status(status)
=======
		except:
			s.error()
>>>>>>> 953a4210b46bb9cb23ac35aaddbf45e21bbf5bb2
