from twitter import *
from random import randint
from time import sleep
from tweepy import TweepError
import sys

api = Twitter()
s = Scraper()
found = False


def generate():
    verse = randint(1,3)
    line = randint(1,3)
    return verse, line


def lyricupdate():
    api.update(lyrics[0] + "\n" + lyrics[1] + "\n\n" + s.url)
    idleperiod = randint(900, 3600)
    print "Sleep for " + str(idleperiod) + " seconds."
    sleep(idleperiod)


def ex():
    sys.exit()

while True:
    while not found:
        verse, line = generate()
        data = s.parser()
        print s.url + " - " + str(s.engexist(data))
        if s.engexist(data):
            lyrics = s.getlyric(data, verse, line)
            if type(lyrics) is not IndexError:
                found = True
                print "\n----------------------------------"
                print lyrics[0] + "\n" + lyrics[1]
                print "----------------------------------\n"
                try:
                    lyricupdate()
                except TweepError:
                        print "Twitter authorization cannot be found. Trying again..."
                        print "Hit Ctrl+C to quit."
                        lyricupdate()
            found = False
            break
