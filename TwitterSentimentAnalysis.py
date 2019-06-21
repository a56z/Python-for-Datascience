import tweepy
from textblob import TextBlob

consumer_key = "D5BBkrpZE0G8rItwfZkmXPVUM"
consumer_secret = "vnnlPsBechhMM5OCuoWhypHLKRbArpXwlijbsZHy4zevft3lPN"

access_token = "940909292357586946-bbOQX28XS9o3pxta7XZSBhWTKbLjR39"
access_token_secret = "em3jjDMG037ugX7eR6Fn94kTuCMVspeCmy1EsffZVRAXA"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search("Trump")

for tweet in public_tweets: 
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)