from bs4 import BeautifulSoup
import requests
import random
import re
from utils import *


class Scraper:

	base = "http://www.animelyrics.com/jpop/"

	def __init__(self):
		self.url = ""


	def getartist(self):
		data = requests.get(self.base).text
		listartist = re.findall("jpop/([a-z]+)",data)
		return random.choice(listartist)

	def getsong(self):
		artist = self.getartist()
		data = requests.get(self.base+artist).text
		listsong = re.findall("%s/([a-z]+)"%artist,data)
		try:
			song = random.choice(listsong)
			return artist, song
		except:
			return self.error()

	def generateurl(self):
		self.artist, self.song = self.getsong()
		self.url = self.base + self.artist + "/" + self.song + ".htm"
		return self.url

	def parser(self):
		try:
			r = requests.get(self.generateurl())
			data = r.text
			soup = BeautifulSoup(data.encode('ascii', 'ignore')) # ignore every ascii in the website
			return soup
		except:
			return self.error()

	def engexist(self, parsed):
		# This will check whether translation exist or not
                try:
                        if parsed.find('th',attrs={'align':'center'}):
                                return True
                        else:
                                return False
                except TypeError:
                        return False

	def getlyric(self, parsed, verse, line):
		byverse = [] # collect the lyrics by verse
		byline = [] # repackage the lyrics by line
		soup = parsed

		# Replace spammy dt tag contains website name with empty string
		for tag in soup.findAll('td', 'translation'):
			tag.find('dt').replace_with("")

		# I don't get how this work but somehow I managed to replace non-ASCII character
		# by using regex although it doesn't make sense at all
		# I think it has something to do with ascii: ignore up there.
		# Nah, regex just replacing \r with \n.
		for tag in soup.findAll('td', 'translation'):
			getverse = (re.sub("\r", "\n", tag.find('span', 'lyrics').text))
			byverse.append(getverse.encode("ascii", "replace_spc")) # custom encode replacing method from utils module

		for item in byverse:
			byline.append(item.split('\n'))
		try:	
			return byline[verse][line], byline[verse][line+1]
		except (IndexError, TypeError) as e:
			return self.error(e)

	def error(self,e=""):
		return e
		pass
		
	



	
