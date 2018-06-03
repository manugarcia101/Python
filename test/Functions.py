# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 21:18:27 2018

@author: Manu
"""

#! Python 3.6.3
#Author: Manuel Garcia Lopez

#function definition & calling
def functionExample():
    print("basic function")
    x = 3 + 2
    print(x)
    
functionExample()

#function parameters
def simple_addition(num1, num2):
    answer = num1 + num2
    print("num1 is", num1)
    print(answer)
    
simple_addition(3,4)

#function default parameters
def simple(num1, num2=4):
    print(num1,num2)
    
simple(5)#prints 5 and 4
simple(3,5)#prints 3 and 5
