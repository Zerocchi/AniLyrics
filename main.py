from lyrics import *
from twitter import *
from random import randint
from time import sleep

api = Twitter()
s = Scraper()
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

        
            

