#!/usr/bin/env python
# Required modules 
import tweepy
from config import *
from time import sleep

# Set up OAuth and integrate with API - your keys need to be in config.py
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

# Create the API
api = tweepy.API(auth)

# This function takes a text file and will read it line by line
# then tweet that line to twitter 
# then sleep ?a day? and do it agian 
# or instead of reading from file, take ouput from any command, ie fortune
def tweet():
    # Open text file for reading
    textFile = 'textFile.txt'
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

tweet()
