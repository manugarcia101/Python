# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 14:12:44 2018

@author: Manu
"""

#! Python 3.6.3
#Author: Manuel Garcia Lopez

#if statement
x = 4
y = 6
z = 3

if x < y:
    print("x is less than y")
    
if z < y > x:
    print("y is greater than z and than x")
    
#Other operators for comparison are: <=, =>, ==, !=

#if - else statement
if x == y:
    print("x is equal than y")
else:
    print("x is not equal than y")
    
#if-elif-else statement
if x > y:
    print("x is greater than y")
elif x < z:
    print("x is greater than z")
elif 5 < x:
    print("5 is smaller than x")
else:
    print("x is greater than none")
    
#In Python there is no switch statement declared