#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 11:13:10 2023

@author: madidina
"""

import pandas as pd
from operator import itemgetter
import csv

# In[]:

# File
df_bid = pd.read_csv('./bid_Price_File_3251758.csv', header=None)
df_offer = pd.read_csv('./offer_Price_File_3251758.csv', header=None)

#File separate into series of price and time
price_bid = df_bid.iloc[:, 1] 
time_bid = df_bid.iloc[:, 0]
price_offer = df_offer.iloc[:, 1]
time_offer = df_offer.iloc[:, 0]

#Convertion from series to array
price_bid_array = price_bid.to_numpy()
price_offer_array = price_offer.to_numpy()
time_offer_array = time_offer.to_numpy()
time_bid_array = time_bid.to_numpy()

# In[]:

def merging (time_offer_array,time_bid_array):
    
    o = len(time_offer_array)
    b = len(time_bid_array)
    
    #offer = np.empty(shape=(a,3))
    offer = []
    #bid = np.empty(shape=(b,3))
    bid = []
    
    for i in range(0,o):
        #offer[i] = [time_offer_array[i],'o',i]
        offer.append([time_offer_array[i],'o',i,0])

    
    for j in range(0,b):
        #bid[j] = [time_bid_array[j],'b',b]
        bid.append([time_bid_array[j],'b',j,0])
    
    merging_array = bid + offer
    res = sorted(merging_array, key = itemgetter(0))
    
    res_bis = [res[0]]
    len_res = len(res)
    
    for i in range(1,len_res,1):
        if res_bis[-1][0]==res[i][0]:
            res_bis[-1][1]='bo'
            res_bis[-1][3]=res[i][2]
        else:
            res_bis.append(res[i])

    return res_bis

# In[]:
    
Final = merging (time_offer_array,time_bid_array)

# CSV file importation 

# field name 
fields = ['Time', 'Offer_Bid', 'Row', 'Offer_Row']

with open('MergedTimeBis', 'w') as f:
      
    # using csv.writer method from CSV package
    write = csv.writer(f)
      
    write.writerow(fields)
    write.writerows(Final)
