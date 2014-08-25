from lyrics import *
from twitter import *
from random import randint
from time import sleep

api = Twitter()
s = Scraper()

def generate():
	verse = randint(0,6)
	line = randint(0,6)
	return verse, line

def post():
	verse, line = generate()
	parse = s.parser()
	if s.engexist(parse):
		status = "\n".join(s.getlyric(parse,verse,line))
		return status
	return None

try:
	while True:
		status = post()
		while status == None or "list index out of range" in status:
			status = post()
		else:
			api.update(status)

		print s.artist, "-", s.song,"\n"	
		print status, "\n"
		sleep(1800)

except KeyboardInterrupt:
	pass
