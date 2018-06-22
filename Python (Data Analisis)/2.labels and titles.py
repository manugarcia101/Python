# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 11:08:54 2018

@author: Manu
"""

#! Python 3.6.5
#Author: Manuel Garcia Lopez

#Matplotlib labels and titles

from matplotlib import pyplot as plt 

x = [5,6,7,8]

y = [7,3,8,3]

plt.plot(x,y)

plt.title('My title')

plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.show()
