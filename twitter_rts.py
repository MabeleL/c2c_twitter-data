# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 13:32:47 2019

@author: Dennis Loyatum
"""

#import the tweepy module
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#user credentials for access of the twitter API
access_token = "423739797-DzRqRuw2m5kO0ZgIVihYtZGeC8Skm27lc2h3ZHs4"
access_token_secret = "XGMaFxJltVk6lNaBvgNWQEvggAYEPABzzt28hqGm8kVZP"
consumer_key = "FZ91sQc0NBdSECv8b9g7xNqf0"
consumer_secret = "Y0RV0ofXnfvOHMZJMwPllC1TUePoNfZGrlBngPd6hJiGzUuix6"

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (status)
        



if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])