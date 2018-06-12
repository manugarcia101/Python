# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 20:04:43 2018

@author: Manu
"""

#!Python 3.6.3
#Author: Manuel García López

#Writing our own generators
'''
Writting our generators can be useful in programs that try 
to find combinations, they make them nicer and don't use
that big amount of memory
'''
'''
A genertor doesn't return values, it yields them
'''
#basic genrator
def simple_gen():
    yield 'Oh'
    yield 'hello'
    yield 'there'
    
for i in simple_gen():
    print(i)
    
#let's say we are looking for the combination of a lock like this
combo_lock = (6, 5, 7)

for c1 in range(10):
    for c2 in range(10):
        for c3 in range(10):
            if (c1, c2, c3) == combo_lock:
                print('Found the correct combo lock: {}'.format((c1,c2,c3)))
                break

'''
to break those 3 loops we would need 3 checks with 3 breaks,
instead we can use a generator
'''

def combo_gen():
    for c1 in range(10):
        for c2 in range(10):
            for c3 in range(10):
                yield (c1, c2, c3)
            
for (c1, c2, c3) in combo_gen():
    if (c1, c2, c3) == combo_lock:
        print('Found the correct combo lock: {}'.format((c1,c2,c3)))
        break
    print(c1, c2, c3)