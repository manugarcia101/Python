# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 19:33:52 2018

@author: Manu
"""

#!Python 3.6.3
#Author: Manuel García López

#list comprehension and generator expressions

'''
List comprehension is gonna be faster on iteration, slower on creation, 
but is gonna be charged on RAM so it can overflow it
Generators on the other hand are slower on iteration, faster on creation 
but they won't use RAM
'''

#let's making them

xyz = [i for i in range(5)] #list generated with 0 to 4

print(xyz)

xyz = []
for i in range(5):
    xyz.append(i)
    
print(xyz)

'''
Both ways do the same as lists comprehensions
How to make generators then? 
    With parenthesis
'''

xyz = (i for i in range(5))
print(xyz) 

'''
the result is gonna be strange now
its an object located pointed by the generator(pointer)
anyway, we can do the same thing as with lists, ex:
'''

for i in xyz:
    print(i)