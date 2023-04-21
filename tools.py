#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 12:16:47 2023

@author: madidina
"""

import pandas as pd
import csv
import numpy as np

from operator import itemgetter

# In[1]:

def merging (bid = 'Data/bid_Price_File_3251758.csv', offer = 'Data/offer_Price_File_3251758.csv'):
    """

    Parameters
    ----------
    bid : string
        path of the file of the bid price ['Time','Price']. The default is 'bid_Price_File_3251758.csv'.
    offer : string
        path of the file of the offer price ['Time','Price']. The default is 'offer_Price_File_3251758.csv'.

    Returns
    -------
    Creation of MergeTime.csv : ['Time', 'Offer_Bid', 'Row', 'Offer_Row']
    'Offer_Bid' = 'b' or 'o'
    'Row' = row of bid or offer concern and 'Offer_Row' = none
     OR 
    'Offer_Bid' = 'bo'
    'Row' = row of bid and 'Offer_Row' = row of offer
    
    """
    # File
    df_bid = pd.read_csv(bid, header=None)
    df_offer = pd.read_csv(offer, header=None)
    
    #File separate into series of time
    time_bid = df_bid.iloc[:, 0]
    time_offer = df_offer.iloc[:, 0]
    
    time_offer_array = time_offer.to_numpy()
    time_bid_array = time_bid.to_numpy()
    
    o = len(time_offer_array)
    b = len(time_bid_array)
    
    offer = []
    bid = []
    
    for i in range(0,o):
        offer.append([time_offer_array[i],'o',i,0])

    
    for j in range(0,b):
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

    # CSV file importation 
    
    # field name 
    fields = ['Time', 'Offer_Bid', 'Row', 'Offer_Row']
    
    with open('MergedTime', 'w') as f:
          
        # using csv.writer method from CSV package
        write = csv.writer(f)
          
        write.writerow(fields)
        write.writerows(res_bis)
 
# In[2]:

def combinaison(MergedTime = 'MergedTime', 
                b_price = 'Data/bid_Price_File_3251758.csv', b_volume = 'Data/bid_Volume_File_3251758.csv', 
                o_price = 'Data/offer_Price_File_3251758.csv', o_volume = 'Data/offer_Volume_File_3251758.csv'):
    """

    Parameters
    ----------
    MergedTime : string, optional
        path of the csv file were we find the time, offer or bid indication, index of the price in the original csv file. 
        The default is 'MergedTime'.
    b_price : string, optional
        path of the original csv file of bid price. 
        The default is 'Data/bid_Price_File_3251758.csv'.
    b_volume : string, optional
        path of the  original csv file of bid volume. 
        The default is 'Data/bid_Volume_File_3251758.csv'.
    o_price : string, optional
        path of the original csv file of offer price. 
        The default is 'Data/offer_Price_File_3251758.csv'.
    o_volume : string, optional
        path of the original csv file of offer volume. 
        The default is 'Data/offer_Volume_File_3251758.csv'.

    Returns
    -------
    None.
    Creation of "LO_File" a csv file of ['Time', 'Bid_Price', 'Bid_Volume', 'Offer_Price', 'Offer_Volume']

    """
    merge_file = open(MergedTime)
    bid_price_file = open(b_price)
    bid_volume_file = open(b_volume)
    offer_price_file = open(o_price)
    offer_volume_file = open(o_volume)
    
    # Read csv: sep default ‘,’
    csv_merge_file = pd.read_csv(merge_file)
    csv_bid_price_file = pd.read_csv(bid_price_file)
    csv_bid_volume_file = pd.read_csv(bid_volume_file)
    csv_offer_price_file = pd.read_csv(offer_price_file)
    csv_offer_volume_file = pd.read_csv(offer_volume_file)
    
    # Init Lists
    total_list=[[0,0,0,0,0]]
    
    print('lists creation')

    for index,row in csv_merge_file.iterrows():
        
        selected_row = row[2]
        
        if (selected_row == len(csv_bid_price_file)) or (selected_row == len(csv_offer_price_file)):
            selected_row-=1
     
        # Acces specific row and coloumn in a csv file
        
        if (row[1]=='b'):
            total_list.append([ csv_bid_price_file.loc[selected_row,:][0],csv_bid_price_file.loc[selected_row,:][1], csv_bid_volume_file.loc[selected_row,:][1], 
                                total_list[-1][3],total_list[-1][4]])
            
        elif (row[1]=='bo'):
            
            if (csv_bid_price_file.loc[selected_row,:][0] < csv_offer_price_file.loc[selected_row,:][0]):
                total_list.append([ csv_bid_price_file.loc[selected_row,:][0],csv_bid_price_file.loc[selected_row,:][1], csv_bid_volume_file.loc[selected_row,:][1],
                                    csv_offer_price_file.loc[selected_row,:][1], csv_offer_volume_file.loc[selected_row,:][1]])

                total_list.append([ csv_offer_price_file.loc[selected_row,:][0],csv_bid_price_file.loc[selected_row,:][1], csv_bid_volume_file.loc[selected_row,:][1],
                                    csv_offer_price_file.loc[selected_row,:][1], csv_offer_volume_file.loc[selected_row,:][1]])
            
            elif (csv_bid_price_file.loc[selected_row,:][0] > csv_offer_price_file.loc[selected_row,:][0]):
                total_list.append([ csv_offer_price_file.loc[selected_row,:][0],csv_bid_price_file.loc[selected_row,:][1], csv_bid_volume_file.loc[selected_row,:][1],
                                    csv_offer_price_file.loc[selected_row,:][1], csv_offer_volume_file.loc[selected_row,:][1]])
                
                total_list.append([ csv_bid_price_file.loc[selected_row,:][0],csv_bid_price_file.loc[selected_row,:][1], csv_bid_volume_file.loc[selected_row,:][1],
                                    csv_offer_price_file.loc[selected_row,:][1], csv_offer_volume_file.loc[selected_row,:][1]])
            
            elif (csv_bid_price_file.loc[selected_row,:][0] == csv_offer_price_file.loc[selected_row,:][0]):
                total_list.append([ csv_bid_price_file.loc[selected_row,:][0],csv_bid_price_file.loc[selected_row,:][1], csv_bid_volume_file.loc[selected_row,:][1],
                                    csv_offer_price_file.loc[selected_row,:][1], csv_offer_volume_file.loc[selected_row,:][1]])
            
        else:
            total_list.append([ csv_offer_price_file.loc[selected_row,:][0],total_list[-1][1], total_list[-1][2],
                                csv_offer_price_file.loc[selected_row,:][1], csv_offer_volume_file.loc[selected_row,:][1]])
            
    # CSV file creation
    print('csv creation')
    
    # field name 
    fields = ['Time', 'Bid_Price', 'Bid_Volume', 'Offer_Price', 'Offer_Volume']
    
    with open('LO_File', 'w') as f:
          
        # using csv.writer method from CSV package
        write = csv.writer(f)
          
        write.writerow(fields)
        write.writerows(total_list)      
        
# In[3]:
  
def extract_spread(LO_File = 'LO_File', spread=1, epsilon=0.5):
    """
    
    Parameters
    ----------
    s : int 
        the value of the spread, set to 1 by default 
        
    epsilon : int
        range of spread 
        
    LO_File : path
        path of the csv file with ['Time', 'Bid_Price', 'Bid_Volume', 'Offer_Price', 'Offer_Volume']
        The default is 'LO_File'
        
    Returns
    -------
    None.
    Creation of the same file with only the lines where spread = s ± epsilon (set at 1±.5 by default)
    
    """    
    
    lo_file = open(LO_File)
    csv_lo_file = pd.read_csv(lo_file)

    # Init Lists
    total_list=[]
    
    print('lists creation')

    for index,row in csv_lo_file.iterrows():
                
        s = row[3] - row[1]
        
        if s < spread+epsilon and s > spread-epsilon:
            total_list.append(row)
    # CSV file creation
    print('csv creation')
    
    # field name 
    fields = ['Time', 'Bid_Price', 'Bid_Volume', 'Offer_Price', 'Offer_Volume']
    
    with open('LO_File_spread', 'w') as f:
          
        # using csv.writer method from CSV package
        write = csv.writer(f)
          
        write.writerow(fields)
        write.writerows(total_list) 
 
# In[4]:

def extract_mo(MO_File = 'Data/MO_File_3251758.csv', LO_File = 'LO_File_spread'):
    """
    Parameters
    ----------
    mo_file : string
        path of the original csv file with th MO: ['Time', 'Type', 'Volume']
    LO_File : string
        path of the csv file with the LO ['Time', 'Type', 'Volume']
    Returns
    -------
    same file with only the lines where time is also in the LO_File
    """    
 
    mo_file = open(MO_File)
    lo_file = open(LO_File)

    csv_mo_file = pd.read_csv(mo_file)
    csv_price_volume_file=pd.read_csv(lo_file)
    
    mo_time, volum_time = [], []
    
    for index, row in csv_mo_file.iterrows():
        mo_time.append(row[0])
    
    for index, row in csv_price_volume_file.iterrows():
        volum_time.append(row[0])
    
    #print(f'There is {len(mo_time)} MO times and {len(volum_time)} same times')
    
    intersection_time = np.intersect1d(mo_time,volum_time)
    print(f'There is {len(intersection_time)} intersection times over {len(mo_time)} MO times')
    
    print('lists creation')

    total = []
    
    for index, row in csv_mo_file.iterrows():
        if row[0] in intersection_time:
            total.append(row)
    
    with open('MO_File', 'w') as f:
          
        # using csv.writer method from CSV package
        write = csv.writer(f)
          
        write.writerows(total) 
        
# In[5]:

def imbalance_truePrice(LO_File = 'LO_File_spread'):
    """

    Parameters
    ----------
    LO_File : string, optional
        path of the csv file of LO. 
        The default is 'LO_File_spread'.

    Returns
    -------
    I: List of imbalance
    T: list of time

    """
    lo_csv = open(LO_File)
    lo = pd.read_csv(lo_csv)

    T = [] # Time List
    I = [] # in [0,1]
    X = [] # True Price List

    print('imbalance list creation')
    for index,row in lo.iterrows():
    
        T.append(row[0])
        
        # I_t = V^b / (V^a + V^b)
        I.append(row[2]/(row[4]+row[2]))
        
        #X_t = B_t + I_t.(A_t-B_t)
        xt = row[1] + I[-1] * (row[4] - row[1])
        X.append(xt)
    
    print('imblance list created')
    return(T, I, X)

# In[6]

def distribution_MO(MO_File = 'Data/MO_File_3251758.csv'):
    """

    Parameters
    ----------
    MO_File : string, optional
        path of the original MO file. 
        The default is 'Data/MO_File_3251758.csv'.

    Returns
    -------
    dV: list of traded volums
    dO: list of theta 
    R: list of the time's ratio rof the MO file over the LO file 

    """
    mo_csv = open(MO_File)
    mo = pd.read_csv(mo_csv)
    
    T, I, X = imbalance_truePrice()
    T = np.array(T)
    
    J  = [0. , 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1. ]
    dV = [0]*10
    dO = [0]*10
    R = []
    error = 0
    
    print('dV creation')
    for index, row in mo.iterrows():
        
        difference_array = np.absolute(T-row[0])
        t = difference_array.argmin()
        gap = T[t] - row[0]
        if (T[t] - T[t-1] != 0) and (T[t+1] - T[t] != 0):

            if gap == 0 :
                #print(difference_array.min())
                difference_array = np.absolute(np.array(J)-I[t])
                j = difference_array.argmin()
                
                if row[1]=='b': 
                    dV[j-1]+= row[2]
                    dO[j-1]+= 1
                elif row[1]=='s':
                    dV[j-1]-= row[2]
                    dO[j-1]-= 1

                R.append(0)
            
            elif gap > 0 : 
                ratio = gap / (T[t] - T[t-1])
                #print(ratio)
                if ratio < 1e-6:
                    difference_array = np.absolute(np.array(J)-I[t])
                    j = difference_array.argmin()
                    
                if row[1]=='b': 
                    dV[j-1]+= row[2]
                    dO[j-1]+= 1
                elif row[1]=='s':
                    dV[j-1]-= row[2]
                    dO[j-1]-= 1
                
                R.append(ratio)
                
            else:
                ratio = - gap / (T[t+1] - T[t])
                #print(ratio)

                if ratio < 1e-6:
                    difference_array = np.absolute(np.array(J)-I[t])
                    j = difference_array.argmin()
                    
                if row[1]=='b': 
                    dV[j-1]+= row[2]
                    dO[j-1]+= 1
                elif row[1]=='s':
                    dV[j-1]-= row[2]
                    dO[j-1]-= 1
                
                R.append(ratio)
            
        else:
                #print(index)
                error +=1
    print(f'there is {error} times where T[t+1] - T[t] or T[t] - T[t-1] is null' ) 
    return(dV, dO, R)

# In[7]

