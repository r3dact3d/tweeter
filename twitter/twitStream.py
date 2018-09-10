#!/usr/bin/env python
import json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = '######################################'
ACCESS_SECRET = '##########################################'
CONSUMER_KEY = '#########################################'
CONSUMER_SECRET = '###########################################'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter Streaming API
twitStream = TwitterStream(auth=oauth)

# List of phrases to track
keywords = ["#resolution", "new year's resolution", "newyear"]

# Get a sample of the public data following through Twitter
#iterator = twitter_stream.statuses.sample()
iterator = twitStream.statuses.filter(track=keywords, language="en", stall_warnings=true, )

# Get data for my specific stream


#twitter_userstream = TwitterStream(auth=oauth, domain='userstream.twitter.com')
# Print each tweet in the stream to the screen 
# Here we set it to stop after getting 1000 tweets. 
# You don't have to set it to stop, but can continue running 
# the Twitter API to collect data for days or even longer. 
tweet_count = 10000000
for tweet in iterator:
    tweet_count -= 1
    # Twitter Python Tool wraps the data returned by Twitter 
    # as a TwitterDictResponse object.
    # We convert it back to the JSON format to print/score
    print json.dumps(tweet)

    # The command below will do pretty printing for JSON data, try it out
    # print json.dumps(tweet, indent=4)

    if tweet_count <= 0:
        break
