# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 14:14:13 2018

@author: Manu
"""

#!Python 3.6.3
#Author: Manuel García López

#Zip
'''
The zip function takes several objs and aggregates them into 
a single one
'''

x = [1, 2, 3, 4] #according to pep8 it is better to give a space between elements
y = [2, 4, 6, 8]
z = ['a', 'b', 'c', 'd']

for a,b in zip(x,y):
    print(a,b) #this stick together the values of x and y
    
print(zip(x,y)) #we can get the zip obj

for i in zip(x,y,z):
    print(i) #we can hold together plenty of different lists
    
print(dict(zip(x,y))) #or a dict

#or use list comprehension
[print(a,b,c) for a,b,c in zip(x,y,z)]#temp variable

#let's see a strange behaviour of python
'''
the thing is that usually, when we declare variables in list 
comprehension by doing the flat way, those vars are temporaries
but, when we do it in the traditional way, with a common for loop
those vars are stored, so this could make us have problems with them
the solution is to take care about the variables we are using
'''
#example of this
for a,b in zip(x,y):
    print(a,b)

print(a)#we should get an error, but we don't

#that happens with every loop we have, so be aware of it!
for d in range(2):
    print(d)
    
print(d)