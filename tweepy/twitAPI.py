import tweepy
from config import *
from time import sleep

# Set up OAuth and integrate with API
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

def findTweet():
    query = '#2017 #newyear'
    for tweet in tweepy.Cursor(api.search, q=query, lang='en', geocode='32.7078750,-96.9209130,100km').items(10):
        try:
            output = 'Tweet by: @' + tweet.user.screen_name + ' > ' + tweet.text
            print output
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break

findTweet()

