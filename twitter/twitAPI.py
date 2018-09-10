#!/usr/bin/env python
# Import the necessary package to process data in JSON format
import json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = '######################################'
ACCESS_SECRET = '##################################'
CONSUMER_KEY = '####################################'
CONSUMER_SECRET = '################################'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter REST API
twitter = Twitter(auth=oauth)

# Search for latest tweets about "#nlproc"
#twitter.search.tweets(q='#dfw')
results = twitter.search.tweets(q='#resolution', result_type='recent', lang='en', count=10)
#dfwTrends = twitter.trends.place(_id = 2388929)

# Get a list of followers of a particular user
#twitter.followers.ids(screen_name="cocoweixu")

# Get a particular user's timeline (up to 3,200 of his/her most recent tweets)
#twitter.statuses.user_timeline(screen_name="billybob")

print json.dumps(results, indent=4)
