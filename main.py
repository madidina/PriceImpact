#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 12:31:28 2023

@author: madidina
"""

from tools import *
import matplotlib.pyplot as plt
import numpy as np

merging()
combinaison()
extract_spread()
xtract_mo()

V, O, R = distribution_MO()

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
