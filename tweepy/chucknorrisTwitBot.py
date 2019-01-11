#!/usr/bin/env python
# written by r3dact3d (brady)
import requests
import tweepy
from random import choice
from config import *

'''
Chucknorris.io is free and will always be! However, as maintaining this service costs $$$,
we are glad to be sponsored by Jugendstil.io.
'''

# Available Catagories - I did this way so specific catagories could be removed if you want... but chuck would not approve.
chuckagories = ["explicit", "dev", "movie", "food", "celebrity", "science", "sport", "political", "religion", "animal", "history", "music", "travel", "career", "money", "fashion"]
chuckagory = choice(chuckagories)

url = 'https://api.chucknorris.io/jokes/random'

# Set up OAuth and integrate with API
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

def tweet(payLoad):
    try:
        print(payLoad)
        if payLoad != '\n':
            api.update_status(payLoad)
        else:
            pass
    except tweepy.TweepError as e:
        print(e.reason)

def chuck(url, params):
    myParams = {
    'query' : params,
    }
    page = requests.get(url, params=myParams)
    if page.status_code == 200:
        output = page.json()
        chuckSays = output['value']
        payLoad = '#chucknorris "%s"' % (chuckSays[:125])
        tweet(payLoad)
    else:
        print('Something went wrong with the API, someone is in big trouble if Chuck finds out!')
        exit()

chuck(url, chuckagory)
