#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 13:46:22 2023

@author: madidina
"""

import pandas as pd
import csv
import numpy as np

merge_file = open('/Users/madidina/Library/Mobile Documents/com~apple~CloudDocs/TELECOM/3A/IIT/MATH-594/SecondStep/MergedTimeBis')
bid_price_file = open('./bid_Price_File_3251758.csv')
bid_volume_file = open('./bid_Volume_File_3251758.csv')
offer_price_file = open('./offer_Price_File_3251758.csv')
offer_volume_file = open('./offer_Volume_File_3251758.csv')

# In[1]:
def combinaison(total_file, b_price_file, b_volume_file, o_price_file, o_volume_file):
    
    """

    Parameters
    ----------
    total_file is the csv file were we find the time, offer or bid indication, index of the price in the original csv file
    b_price/volume_file are the original csv file of bid price / volume 
    o_price/volume_file are the original csv file of offer price / volume

    Returns
    -------
    Creation of "LO_File" a csv file of ['Time', 'Bid_Price', 'Bid_Volume', 'Offer_Price', 'Offer_Volume']
    """
    
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
        
       
#combinaison(merge_file, bid_price_file, bid_volume_file, offer_price_file, offer_volume_file)

# In[2]
    
lo_file = open('/Users/madidina/Library/Mobile Documents/com~apple~CloudDocs/TELECOM/3A/IIT/MATH-594/SecondStep/LO_File')

def extract_spread(Price_Volume_File, spread=1, epsilon=0.5):
    """
    
    Parameters
    ----------
    s : int 
        the value of the spread, set to 1 by default 
        
    epsilon : int
        range of spread 
        
    Price_Volume_File : csv
        ['Time', 'Bid_Price', 'Bid_Volume', 'Offer_Price', 'Offer_Volume']

    Returns
    -------
    same file with only the lines where spread = s ± epsilon (set at 1±.5 by default)
    
    """    
    
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
     
#extract_spread(lo_file)

 # In[3]

mo_file = open('/Users/madidina/Library/Mobile Documents/com~apple~CloudDocs/TELECOM/3A/IIT/MATH-594/SecondStep/MO_File_3251758.csv')
lo_file_spread = open('LO_File_spread')

     
def extract_mo_spread(mo_file, lo_file_spread):
    """
    Parameters
    ----------
    mo_file : csv
        ['Time', 'Type', 'Volume']
    lo_file_spread : csv
        ['Time', 'Type', 'Volume']
    Returns
    -------
    same file with only the lines where time is also in the lo_file_spread

    """    
 
    csv_mo_file = pd.read_csv(mo_file)
    csv_price_volume_file=pd.read_csv(lo_file_spread)
    
    mo_time, volum_time = [], []
    
    for index, row in csv_mo_file.iterrows():
        mo_time.append(row[0])
    
    for index, row in csv_price_volume_file.iterrows():
        volum_time.append(row[0])
    
    print(f'There is {len(mo_time)} MO times and {len(volum_time)} spread times')
    
    intersection_time_spread1 = np.intersect1d(mo_time,volum_time)
    print(f'There is {len(intersection_time_spread1)} intersection times')
    
    print('lists creation')

    total = []
    
    for index, row in csv_mo_file.iterrows():
        if row[0] in intersection_time_spread1:
            total.append(row)
    
    with open('MO_File_spread', 'w') as f:
          
        # using csv.writer method from CSV package
        write = csv.writer(f)
          
        write.writerows(total) 
  
extract_mo_spread(mo_file, lo_file_spread)
