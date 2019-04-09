# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 00:04:21 2019

@author: Dennis Loyatum
"""

#importing modules and libraries
from copy import deepcopy
import numpy as np
import pandas as pd

from matplotlib import pyplot as plt
plt.rcParams['figure.figsize'] = (16,9);
plt.style.use('ggplot')

#importing the datasets
raw_data = pd.read_csv ("c2c2data.csv")
#print (raw_data)
print(raw_data.shape)

#Getting the values in the numpy array and grouping it

f1 = raw_data['retweet_count'].values
f2 = raw_data['followers_count'].values
f3 = raw_data['friends_count'].values
f4 = raw_data['subscribed_count'].values
f5 = raw_data['statuses_count'].values
f6 = raw_data['liked_tweets_count'].values
f7 = raw_data['Trust score'].values

#clean the data and present it nicely in an array
X = np.array(list(zip(f1,f2,f3,f4,f5,f6,f7)))
print(X)

#create an object for when a twitter account was created
raw_data['account_created_at'] =  pd.to_datetime(raw_data['account_created_at'],
                              dayfirst=True)
