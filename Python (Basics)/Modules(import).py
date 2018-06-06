# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 12:53:37 2018

@author: Manu
"""

#! Python 3.6.3
#Author: Manuel Garcia Lopez

#Modules import
import statistics as s #we can create an alias for each of our imports
#also we can import everything in another way
from statistics import *
#we can also just import the thing we want from the proper import 
from statistics import mean
#we could even say the following using another alias
from statistics import stdev as st
#or just import several functions form one module in one single time with alias 
from statistics import median as m, median_low as ml

sample_list = [1,2,3,4,5,23,56,6,7,8,9]

variance = s.variance(sample_list)
mean1 = mean(sample_list)
stdev1 = st(sample_list)
median = m(sample_list)
medianl = ml(sample_list)

print(variance)
print(mean1)
print(stdev1)
print(median)
print(medianl)

#Using our own modules
import ModulesCreation

ModulesCreation.ex('test')