# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 10:04:38 2018

@author: Manu
"""

#! Python 3.6.5
#Author: Manuel Garcia Lopez

#Scatter plots
from matplotlib import pyplot as plt 

x = [5,6,7,2]
y = [1,3,8,3]

x2 = [5,6,5,8]
y2 = [7,6,8,3]

#displaying exacts dots
plt.scatter(x,y ,color = 'c')
plt.scatter(x2,y2 ,color = 'g')

#displaying columns
plt.bar(x,y ,color = 'c')
plt.bar(x2,y2 ,color = 'g')

plt.title('My title')

plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.show()