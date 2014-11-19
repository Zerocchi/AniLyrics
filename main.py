from lyrics import *
from twitter import *
from random import randint
from time import sleep

api = Twitter()
s = Scraper()
<<<<<<< HEAD
found = False

def generate():
	verse = randint(1,3)
	line = randint(1,3)
	return verse, line

while True:
    while found == False:
        verse, line = generate()
        data = s.parser()
        print s.url + " - " + str(s.engexist(data))
        if s.engexist(data) == True:
            lyrics = s.getlyric(data, verse, line)
            if type(lyrics) is not IndexError:
                found = True
                print "\n----------------------------------"
                print lyrics[0] + "\n" + lyrics[1]
                print "----------------------------------\n"
                api.update(lyrics[0] + "\n" + lyrics[1] + "\n\n" + s.url)
                idleperiod = randint(900,3600)
                print "Sleep for " + str(idleperiod) + " seconds."
                sleep(idleperiod)
            found = False
            break

        
            

=======

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
>>>>>>> 953a4210b46bb9cb23ac35aaddbf45e21bbf5bb2
