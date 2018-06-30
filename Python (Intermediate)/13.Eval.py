# -*- coding: utf-8 -*-
"""
Editor de Spyder

@author: Manu
"""

#!Python 3.6.5
#Author: Manuel García López

#Eval python module
'''
It evaluates an expression and it returns the value,
it is used to parse smth in string form 
'''
list_str = "[2,5,9,1,5]"

list_str = eval(list_str)

print(list_str)
print(list_str[2])

'''
We can also check expressions as 5 < 10 for example
'''
check_out = eval(input("code:"))
print(check_out)