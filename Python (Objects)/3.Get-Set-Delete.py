# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 10:21:27 2018

@author: Manu
"""

#! Python 3.6.3
#Author: Manuel Garcia Lopez

#Property Decorators (Get,Set,Delete)
'''
In some languages as Java or C++, we are able to define
getters and setters as special methods to alter correctly some
of the objects attribute values, in Python, we will do something 
similar, but using properties, which will allow us to change the 
value more directly, let's see it
'''
class Employee(object):
    
    #constructor 
    def __init__(self, first, last, pay): 
        self.first = first
        self.last = last
        self.pay = pay
        
    #methods
    @property #each time we add this, we are making the obj readable
    def email(self):#in this case this works as getter
        return '{}_{}@gmail.com'.format(self.first, self.last)
    
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @fullname.setter #setter
    def fullname(self,name):
        first,last = name.split(' ')
        self.first = first
        self.last = last
    
    @fullname.deleter #deleter
    def fullname(self):
        print('Deleting fullname!')
        self.first = None
        self.last = None

emp_1 = Employee('Corey','Schafer',900)

#emp_1.fullname = 'Manu Garcia'
del emp_1.fullname

print(emp_1.first)
print(emp_1.email)#with property tag we don't need to use parenthesis
print(emp_1.fullname)