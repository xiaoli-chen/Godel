#from twython import Twython
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
import json


CONSUMER_KEY = 'pxeqo0ylpUayIIl5Nlc2kBmkb'
CONSUMER_SECRET = 'JUAAG5ilMS9TxZN1Y0ZKwPhsamtE3gFoIYTnKfwWTGqGmF6zXL'
ACCESS_TOKEN = '395150986-GiB9RbBtrjjiEetZ977wtQwYGVWCuhiPMir0962F'
ACCESS_SECRET = 'DUk5aVVGGy55PySqjVNMWV4MTghtvdfwXbDJROUEnrH9Y'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter REST API
twitter = Twitter(auth=oauth)
            
# Search for latest tweets about "#nlproc"
twitter.search.tweets(q='#nlproc')

#twitter.search.tweets(q='#nlproc', result_type='recent', lang='en', count=10)

