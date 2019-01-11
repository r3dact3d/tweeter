#!/usr/bin/env python
# written by brady [r3dact3d]
import tweepy, os
from config import *

# Set up OAuth and integrate with API
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

def tweet():
    cmd = 'fortune -sae'
    proc = os.popen(cmd)
    result = str(proc.read())
    fortune = '%s ...#fortune' % result
    try:
        print(fortune)
        if fortune != '\n':
            api.update_status(fortune)
        else:
            pass
    except tweepy.TweepError as e:
        print(e.reason)

tweet()
