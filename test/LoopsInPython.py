# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 13:42:30 2018

@author: Manu
"""
#! Python 3.6.3
#Author: Manuel Garcia Lopez

#first we will see some examples of how declare and use
#some variables

exampleVar = 50
exampleVar2 = "Hej hej"
exampleVar3 = True

print(exampleVar)
print(exampleVar2)
print(exampleVar3)

x,y,z = (3,2,5)

print(x)
print(y)
print(z)

#while loop
counter = 1

while counter < 10:
    print(counter)
    counter += 1
    
#for loop
exampleList = [1,2,3,4,5,6,7,8,9]

for each in exampleList:
    print(each)
    
for x in range(1,11):
    print(x)
'''
As far as python works not with curly braces but with code
identation, we need to be careful with it, in loops or if/else 
statements, to exit them, we need to break this identation
'''