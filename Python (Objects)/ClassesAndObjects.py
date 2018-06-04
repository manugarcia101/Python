# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 19:46:30 2018

@author: Manu
"""

#! Python 3.6.3
#Author: Manuel Garcia Lopez

#Classes in Python
#Basic class example with some easy methods
class calculator:
    
    def addition(x,y):
        added = x + y
        print(added)
    
    def substraction(x,y):
        sub = x - y
        print(sub)
        
    def multiplication(x,y):
        mult = x*y
        print(mult)
        
    def division(x,y):
        div = x/y
        print(div)
        
#call to the class methods
calculator.addition(3,7)
calculator.substraction(3,7)
calculator.multiplication(3,7)
calculator.division(3,7)