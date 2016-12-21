#!/usr/bin/env python

import tweepy
import sys
from config import *

class CustomStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        #print('Tweet: ' + status.user.screen_name + ' > ' + status.text)
        print(status)
    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream

# Set up OAuth and integrate with API
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.streaming.Stream(auth, CustomStreamListener())
api.filter(track=['#resolution'])

