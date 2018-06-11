# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 13:10:29 2018

@author: Manu
"""

#!Python 3.6.3
#Author: Manuel García López

#Timeit Module

'''
A way of measuring the time smth takes on it's execution
could be: 
start = time.time()
total = time.time() - start
but we are going to use a more precise temp measuring and it would
be with Timeit
'''

import timeit

#quick example of timeit lib
print(timeit.timeit('1+3', number = 5000))#number is how many times we do the action

inputList = range(100)

def divisibleByFive(num):
    if num % 5 == 0:
        return True
    else:
        return False

xyz = (i for i in inputList if divisibleByFive(i))

xyz1 = [i for i in inputList if divisibleByFive(i)]

print(timeit.timeit('''inputList = range(100)

def divisibleByFive(num):
    if num % 5 == 0:
        return True
    else:
        return False

xyz = (i for i in inputList if divisibleByFive(i))

xyz1 = [i for i in inputList if divisibleByFive(i)]''', number = 500))
    
'''
the problem of using it seems obvious, we have to test all the snipet
of code inside the function but for testing, is a quite good option
'''

#let's see another example comparing how long it takes 
#iteration in case of gens or lc

#gen
print(timeit.timeit('''inputList = range(100)

def divisibleByFive(num):
    if num % 5 == 0:
        return True
    else:
        return False

xyz = (i for i in inputList if divisibleByFive(i))

for i in xyz:
    x = i''', number = 5000))

#lc
print(timeit.timeit('''inputList = range(100)

def divisibleByFive(num):
    if num % 5 == 0:
        return True
    else:
        return False

xyz = [i for i in inputList if divisibleByFive(i)]

for i in xyz:
    x = i''', number = 5000))