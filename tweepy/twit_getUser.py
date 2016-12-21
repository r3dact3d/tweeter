#!/usr/bin/env python

import tweepy
from time import sleep
from config import *

# Set up OAuth and integrate with API
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

freeList = '/home/itsbt/tweepy/userNames.txt'
oFile = open(freeList, 'r')
names = []
for line in oFile:
    line = line.strip('\n')
    names.append(line)
oFile.close()

for name in names:
    user = api.get_user(name, include_entities=1)
    try:
        print(user)

    except tweepy.TweepError as e:
        print(e.reason)

