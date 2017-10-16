#from twython import Twython
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
import json


CONSUMER_KEY = 'pxeqo0ylpUayIIl5Nlc2kBmkb'
CONSUMER_SECRET = 'JUAAG5ilMS9TxZN1Y0ZKwPhsamtE3gFoIYTnKfwWTGqGmF6zXL'
ACCESS_TOKEN = '395150986-GiB9RbBtrjjiEetZ977wtQwYGVWCuhiPMir0962F'
ACCESS_SECRET = 'DUk5aVVGGy55PySqjVNMWV4MTghtvdfwXbDJROUEnrH9Y'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)


# Initiate the connection to Twitter Streaming API
twitter_stream = TwitterStream(auth=oauth)

# Get a sample of the public data following through Twitter
iterator = twitter_stream.statuses.sample()


# the Twitter API to collect data for days or even longer. 
tweet_count = 1000
for tweet in iterator:
    tweet_count -= 1
    # Twitter Python Tool wraps the data returned by Twitter 
    # as a TwitterDictResponse object.
    # We convert it back to the JSON format to print/score
    print(json.dumps(tweet))
    
    # The command below will do pretty printing for JSON data, try it out
    # print json.dumps(tweet, indent=4)
       
    if tweet_count <= 0:
        break 
