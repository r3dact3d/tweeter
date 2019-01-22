#!/usr/bin/env python
# written by brady [r3dact3d]
from bs4 import BeautifulSoup
import requests
import tweepy
from config import *

url = 'http://www.urbandictionary.com/'
page = requests.get(url)
soup = BeautifulSoup(page.text, "lxml")
data = dict()
data['def'] = soup(class_ = 'meaning')[0].text
data['word'] = soup(class_ = 'word')[0].text
word = data['word'].strip('u').strip('\n')
meaning = data['def'].strip('u').strip('\n')
short = 'https://goo.gl/gZMF'

payLoad = 'Daily #UrbanDictionary> %s: %s ... %s' % (word, meaning[:65], short)

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

tweet(payLoad)
