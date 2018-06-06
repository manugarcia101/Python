# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 12:42:34 2018

@author: Manu
"""

#! Python 3.6.3
#Author: Manuel Garcia Lopez

#statistics with Python
import statistics

sample_list = [1,2,3,4,5,23,56,6,7,8,9]

mean = statistics.mean(sample_list) #average
median = statistics.median(sample_list)
standard_deviation = statistics.stdev(sample_list)
variance = statistics.variance(sample_list)

print(mean)
print(median)
print(standard_deviation)
print(variance)

'''
The total function list is:
mean()	Arithmetic mean (“average”) of data.
harmonic_mean()	Harmonic mean of data.
median()	Median (middle value) of data.
median_low()	Low median of data.
median_high()	High median of data.
median_grouped()	Median, or 50th percentile, of grouped data.
mode()	Mode (most common value) of discrete data.

Spread functions

pstdev()	Population standard deviation of data.
pvariance()	Population variance of data.
stdev()	Sample standard deviation of data.
variance()	Sample variance of data.	
'''