# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 21:33:06 2018

@author: Manu
"""

#! Python 3.6.3
#Author: Manuel Garcia Lopez

#global variable

global y #not recommended to use

#local variable

x = 6

def example():
    print(x)
    #we could not do x+=1 if x as long as x is not global
    globx = x+1 #auxiliar local variable
    print(globx)
    return globx
    
x = example()