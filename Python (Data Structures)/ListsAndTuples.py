# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 18:47:03 2018

@author: Manu
"""

#! Python 3.6.3
#Author: Manuel Garcia Lopez

#Lists and Tuples
'''
First of all, which is the difference in their meaning?
A tuple is inmutable, you can not change it's order,
you can not change it's size, it's elements etc
While a list is mutable, which means you can "play" 
with it's data

Advantages of tuples: 
They are created and iterated faster than lists

Advantages of lists:
They are simply mutables
'''

#tuple examples
x = 4,6,7,8,2
x1 = (2,34,6,84,2)

#list examples (basic ones)
y = [5,6,4,7,8,1,1]
y1 = y
y2 = [12,3,5,1]

#how to access data inside tuples
print(x[0])#first element of the tuple
print(x[1:6])#prints (6,7,8,2) the last element the sixth is not included

#to update a tuple we need to create a new one, as far we can't modified tuples data
x2 = x + x1 #concatenating tuples
print(x2[0:11])#tuples iteration never goes out of bounds

#deleting tuples
del x1

#basic tuples operations
#length
print(len(x))
#concatenation
x2 = x2 + x
#repetition
print(x*3)
#membership
print(2 in x)
#iteration
for z in x: print(z)

#tuple functions
print(max(x))#print max element of a tuple
print(min(x))#print min element of a tuple
tuple(y)#converts a list into a tuple

#how to access data inside a list
print(y[0])#first element of the list
print(y[1:6])

#updating lists
print(y[2])
y[2] = 98
print(y[2])

#deleting lists
del y1

#basic lists operations
#the same as tuples
#length
print(len(y2))
#concatenation
y2 = y2 + y
#repetition
print(y*3)
#membership
print(2 in y)
#iteration
for z in y: print(z)

#list functions
print(max(y))#print max element of a list
print(min(y))#print min element of a list
list(x)#converts a tuple into a list

#list methods
y.append(221) #Appends object obj to list
y.count(1) #Returns count of how many times obj occurs in list
#we create the following sequence
seq = [1,2,3]
y.extend(seq) #Appends the contents of seq to list
y.index(2) #Returns the lowest index in list that obj appears
y.insert(5,23) #Inserts object obj into list at offset index, if index is so big or none, it will append the data to the end
y.pop() #Removes and returns last object or obj from list
y.remove(1) #Removes object obj from list
y.reverse() #Reverses objects of list in place
y.sort() #Sorts objects of list, use compare func if given, you can pass a sort function as a parameter to sort