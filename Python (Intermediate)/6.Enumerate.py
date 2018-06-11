# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 14:03:40 2018

@author: Manu
"""

#!Python 3.6.3
#Author: Manuel García López

#Enumerate
'''
Basically we are going to try to return a tuple, with th count
of how many times an object is inside somewhere, and the obj
'''

example = ['left','right','up','down']

#this is not the right way of printing smth
for i in range(len(example)):
    print(i,example[i])
    
#the right way is this:
#why? Because it is nicer and we will expect a result more accurate 
#to the reality
for i,j in enumerate(example):
    print(i,j)
    
#another example of using an enumerate over a dict
newDict = dict(enumerate(example))
print(newDict)

[print(i,j) for i,j in enumerate(newDict)]