import tweepy
from textblob import TextBlob

consumer_key = 'bfKZVJBDaV0INndwNl6fZgGQz'
consumer_secret ='girk9lOHRLZr52uQ8sjlayxbtEDKBCzYrbc2u4A5eQ0jIJMElQ' 
access_token = '2945143285-15EppRatT7fqLsL1PEGVSerhT1yjJr1e9pmHEPs'
access_token_secret = 'BENchB82GBxFSazGB9Bjtju3ut5cj6jjsbTHMevbchLZ2'
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)
public_tweets = api.search('Trump')
for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
