#!/usr/bin/env python

# Tweets the most recent posts to a Pinboard account in the past 30 minutes.
# Avoids Tweeting twice by storing recently-Tweeted posts in an array and
# checking against it after each update. 

import pinboard
import datetime
import emoji
import tweepy

pbtoken = 'YOUR-PINBOARD-API-TOKEN'
consumer_key = 'TWITTER-APP-CONSUMER-KEY'
consumer_secret = 'TWITTER-APP-CONSUMER-SECRET'
access_key = 'TWITTER-APP-ACCESS-KEY'
access_secret = 'TWITTER-APP-ACCESS-SECRET'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
twitter = tweepy.API(auth)

pb = pinboard.Pinboard(pbtoken)
symbol = emoji.emojize(':eyeglasses:')
tweeted = []

def shouldWeBother(): 
    # Check the last pinboard update time.
    now = datetime.datetime.utcnow() 
    delta = now - pb.posts.update()
    time_period = 30 * 60 
    return delta.total_seconds > time_period

def getPosts():
    # If the last update time is in the past 90 minutes:
    if update:
        # Get a new batch of posts.
        timeframe = datetime.datetime.utcnow() - datetime.timedelta(minutes=30)
        posts = pb.posts.all(fromdt=timeframe)
        return posts

def evaluatePosts():
    # Evaluate each post in this new batch
    for post in getPosts():
        # If the post is not in the "tweeted" array, Tweet it and add it to the
        # store array
        if not post in tweeted:
            s = " ";
            seq = (symbol, post.description, post.url);
            message = s.join(seq)
            twitter.update_status(message)
            tweeted.append(post)

update = shouldWeBother()
evaluatePosts()