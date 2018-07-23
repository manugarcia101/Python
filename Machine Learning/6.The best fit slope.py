# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 19:57:28 2018

@author: Manu
"""

#!Python 3.6.3
#Author: Manuel García López

#Machine Learning
from statistics import mean
import numpy as np
import matplotlib.pyplot as plt

xs = np.array([1,2,3,4,5,6], dtype = np.float64)
ys = np.array([5,4,6,5,6,7], dtype = np.float64)

def best_fit_slope(xs,ys):
    
    m = (((mean(xs) * mean(ys)) - mean(xs*ys)) / 
         ((mean(xs) * mean(xs)) - mean(xs*xs)))
    
    return m

m = best_fit_slope(xs,ys)

print(m)