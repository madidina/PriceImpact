#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 10:00:44 2023

@author: madidina
"""

import pandas as pd
#import csv
import numpy as np
import matplotlib.pyplot as plt

lo_csv = open('/Users/madidina/Library/Mobile Documents/com~apple~CloudDocs/TELECOM/3A/IIT/MATH-594/SecondStep/LO_File_spread')
mo_csv = open('/Users/madidina/Library/Mobile Documents/com~apple~CloudDocs/TELECOM/3A/IIT/MATH-594/SecondStep/MO_File_3251758.csv')

lo = pd.read_csv(lo_csv)
mo = pd.read_csv(mo_csv)

# In[1]

def imbalance(file):
    T = [] # Time List
    I = [] # in [0,1]
    print('imabalance creation')
    for index,row in lo.iterrows():
    
        T.append(row[0])
        
        # I_t = V^b / (V^a + V^b)
        I.append(row[2]/(row[4]+row[2]))
    
    print('imbalance created')
    return(I,T)

I, T = imbalance(lo)

# In[2]

def distribution_MO(mo_file,I, T):
    
    J  = [0. , 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1. ]
    dV = [0]*10
    dO = [0]*10
    T = np.array(T)
    R = []
    error = 0
    
    print('dV creation')
    for index, row in mo_file.iterrows():
        
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

V, O, R = distribution_MO(mo, I, T)

X = np.array(["0.1", "0.2", "0.3", "0.4", "0.5", "0.6", "0.7", "0.8", "0.9", "1"])
Y = np.array(np.absolute(V))
Z = np.array(np.absolute(O))

plt.bar(X,Y)
plt.title('Distribution of traded volume across imbalance levels, when the spread = 1±.5')
plt.show()

plt.bar(X,Z)
plt.title('Distribution of theta across imbalance levels,when the spread = 1±.5')
plt.show()

#plt.hist(R) #ratio in null
