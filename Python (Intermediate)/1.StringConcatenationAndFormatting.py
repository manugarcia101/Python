# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 17:59:23 2018

@author: Manu
"""

#Strings: concatenation and formatting

'''
Let's see another way of concatenating strings, till now
so far we have seen how to concatenate with the sign '+'
'''
names = ['Jeff','Gary','Jill','Samantha']

for name in names:
    #print('Hello there, '+ name)
    #old way of concatenating, although it is more readable
    print(' '.join(['Hello there, ',name]))
    #better way of concatenating
    
print(','.join(names)) 
'''
this way is even better, is readable if you know what join is, 
is flat and it's short
join is a function used to concatenating more than 2 strings
with less processing
'''

import os 

locationFile = 'C:\\Users\\Manu\\Desktop'
fileName = 'example.txt'

print(locationFile + '\\' + fileName) #old way 

#other way of using the join function, better way of use it 
with open(os.path.join(locationFile,fileName)) as f:
    print(f.read())
    
#string formatting
who = 'Gary'
howMany = 12
#expected sentence
#Gary bought 12 apples today!
print(who, 'bought', howMany, 'apples today!') #old way

#using the function .format, it's also better
print('{0} bought {1} apples today!'.format(who,howMany))
#to establish an order we can use numbers for it inside the curly braces