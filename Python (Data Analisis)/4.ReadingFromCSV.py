# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 10:22:47 2018

@author: Manu
"""
#! Python 3.6.5
#Author: Manuel Garcia Lopez

#Reading data from csv
from matplotlib import pyplot as plt 
import numpy as np

x,y = np.loadtxt('Matplotlib.csv', unpack = True, 
                 delimiter = ',')

plt.plot(x,y)

plt.title('My title')

plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.show()