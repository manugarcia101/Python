# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 12:33:59 2018

@author: Manu
"""

#!Python 3.6.3
#Author: Manuel García López

#More on list comprehension and generators

xyz = [i for i in range(50000)]
print('done')

xyz = (i for i in range(50000))
print(xyz)

'''
Up, we have the summary of what we saw in the first example
of Generators and list comprehension, and now we are going to
see how to manipulate those objects without really creating them
'''

inputList = [3,4,3,1,5,7,30,7,5]

def divisibleByFive(num):
    if num % 5 == 0:
        return True
    else:
        return False

#let's make the generator with only the numbers divisibles by 5
xyz = (i for i in inputList if divisibleByFive(i))

#and also the list would be
'''
xyz = []
for i in inputList:
    if divisibleByFive(i):
        xyz.append(i)
'''

#we could show the results in the common way
for i in xyz:
    print(i)

#or we can do it following the beauty code rules of pep8
#this is almost always better
[print(i) for i in xyz]

#let's see now how to work with matrices in lc and gen
#the tradicional way fulling a matrix would be like:
xyx = []
for i in range(5):
    for ii in range(5):
        print(i,ii)
        #xyx.append(ii)
        
#print(xyx)

#but with lc for example could be just one line:
[[print(i,ii)for ii in range(5)] for i in range(5)]

#another thing we could do is something like this:
xyz = (print(i) for i in range(5))

for i in xyz:
    i#we are not printing i but showing i beacuse each gen element 
     #is already printing i