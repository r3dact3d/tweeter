#!/usr/bin/env python

import json
from sys import argv

script, tweetFile = argv
tweetRead = open(tweetFile, "r")

for line in tweetRead:
    try:
        # Read in one line of the file, convert it into a json object 
        tweet = json.loads(line.strip())
        if 'text' in tweet: # only messages contains 'text' field is a tweet
            print tweet['id'] # This is the tweet's id
            print tweet['created_at'] # when the tweet posted
            print tweet['text'] # content of the tweet
            print tweet['user']['id'] # id of the user who posted the tweet
            print tweet['user']['name'] # name of the user
            print tweet['user']['screen_name'] # name of the user account
            print tweet['user']['location']          
            hashtags = []
            for hashtag in tweet['entities']['hashtags']:
                hashtags.append(hashtag['text'])
            print hashtags

    except:
        # read in a line is not in JSON format (sometimes error occured)
        continue
