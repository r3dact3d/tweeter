import tweepy
from config import *
from time import sleep

# Set up OAuth and integrate with API
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

def tweet():
    # Open text file for reading
    textFile = '/home/itsbt/working/textFile.txt'
    readFile = open('textFile', 'r')
    readLine = readFile.readlines()
    readFile.close()

    for line in readLines:
        try:
            print(line)
            if line != '\n':
                api.update_status(line)
                sleep(3600)
            else:
                pass
        except tweepy.TweepError as e:
            print(e.reason)
            sleep(3600)

#tweet()
