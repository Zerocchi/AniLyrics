from twitter import *
from random import randint
from time import sleep
from tweepy import TweepError
from utils import ex

api = Twitter()
s = Scraper()
found = False
retry_counter = 3


def generate():
    verse = randint(1,3)
    line = randint(1,3)
    return verse, line


def lyricupdate():
    api.update(lyrics[0] + "\n" + lyrics[1] + "\n\n" + s.url)
    idleperiod = randint(900, 3600)
    print "Sleep for " + str(idleperiod) + " seconds."
    sleep(idleperiod)

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
                while retry_counter > 0:
                    try:
                        lyricupdate()
                        found = False
                        break
                    except TweepError:
                            print "Cannot post tweet. Retrying..."
                            retry_counter -= 1
                            sleep(5)
                            continue
                else:
                    print "Twitter authorization failed. Please double check your twitter.py credentials."
                    ex()