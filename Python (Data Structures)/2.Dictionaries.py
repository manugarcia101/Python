# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 18:44:17 2018

@author: Manu
"""

#!Python 3.6.3
#Author: Manuel Garcia Lopez

#Dictionaries

'''
As we may know, dictionaries are data strutures like maps or 
trees, that can search for key, let's see how do the work
'''

sampleDict = {'Jack':20,'Bob':23,'Alice':32,'Rachel':8}

#we can extract data using the key, in this case, the name
print(sampleDict['Jack'])

#adding
#we can create and add new entries to the dictionary like this:
sampleDict['Tim'] = 14
print(sampleDict['Tim'])

#updating
#we just change the value of the key
sampleDict['Tim'] = 15
print(sampleDict['Tim'])

#deleting
#we just delete the object tim of the dictionary
del sampleDict['Tim']

#we can also insert lists inside the object part of each value of the dictionary
sampleDict1 = {'Jack':[20,'blonde'],'Bob':[23,'red'],'Alice':[32,'blonde'],
               'Rachel':[8,'dark']}

print(sampleDict1['Jack'])
print(sampleDict1['Jack'][1])

'''
It is also possible to asign not a list, but another dictionary, or function or
complex object to the value of each position of the dictionary
'''

'''
Properties of Dictionary keys:
    
1-More than one entry per key is not allowed
2-Keys must be inmutable
'''
#Functions and methods
#functions
len(sampleDict)#Gives the total length of the dictionary. This would be equal to the number of items in the dictionary.
str(sampleDict)#Produces a printable string representation of a dictionary
type(sampleDict) #Returns the type of the passed variable. If passed variable is dictionary, then it would return a dictionary type.

#methods
sampleDict.clear()#Removes all elements of dictionary dict
sampleDict.copy()#Returns a shallow copy of dictionary dict
seq = ('Jack','Pepe')
sampleDict.fromkeys(seq,2)#Create a new dictionary with keys from seq and values set to value.
sampleDict.get('Jack')#For key Jack, returns value or default if key not in dictionary
sampleDict.items()#Returns a list of dict's (key, value) tuple pairs
sampleDict.keys()#Returns list of dictionary dict's keys
sampleDict.setdefault('Jack')#Similar to get(), but will set dict[key]=default if key is not already in dict
sampleDict.update(sampleDict1)#Adds dictionary dict2's key-values pairs to dict
sampleDict.values()#Returns list of dictionary dict's values