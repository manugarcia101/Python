# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 19:46:30 2018
@author: Manu
"""

#! Python 3.6.3
#Author: Manuel Garcia Lopez

'''
Magic Methods:
Magic methods are those that are used in a special
way and with different behaviours depending on 
the object used, for example: initis a special 
method, those methods are usually surrounded by
double dunderscore (__)
'''
class Employee:
    
    #class variables for Employee
    raise_amount = 1.01
    
    #constructor 
    def __init__(self, first, last, pay): 
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '_' + last +'@gmail.com'
        
    #methods
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)
        
    #special methods (repr and str, good methods to have on our code)
    '''
    repr is meant to be a representation of an 
    unambiguous object, it should be use for debugging,
    logging and things like that
    '''
    def __repr__(self):
        return "Employee('{}','{}','{}')".format(self.first, self.last, self.pay)
    
    '''
    str is meant to be more like a readable representation 
    of an object, is meant to be use as a diplay to the 
    end user
    '''
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)
    
    def __add__(self, other):
        '''
        Even when that is not the case, it is very common to
        check some stuff and see if smth is expected or not, 
        ehen smth is not, we usually raise an error, but 
        sometimes, we don't want to raise it, cause we know 
        that some class from the outside scope of the variable
        is gonna be able to handle it, in that case instead 
        throwing an error, we just return NotImplemented
        '''
        if isinstance(other, Employee):
            return self.pay + other.pay
        return NotImplemented
    
    def __len__(self):
        return len(self.fullname())

#instances    
emp_1 = Employee('Corey','Schafer',900)
emp_2 = Employee('Manu','Garcia',1000)

print(emp_1) #this is calling directly to str
            #if str is not there, it calls to repr
            
#other ways of calling that methods more visually
#way number 1
print(repr(emp_1))
print(str(emp_1))

#way number 2
print(emp_1.__repr__())
print(emp_1.__str__())

'''
we can also use the dunder methods of an already
defined class as integer or string, ex:
'''
print(int.__add__(1, 2)) #It returns 3 due to the addition of 1 plus 2
print(str.__add__('a', 'b')) #returns ab
print(len('test')) #not dunder, returns lenght of the array
print('test'.__len__()) #dunder, also returns the lenght

print(emp_1 + emp_2) #makes the salary sum of 1 and 2, it uses the dunder method add
print(emp_1.__len__()) #dunder len for our obj
print(len(emp_1)) #the other not dunder call

'''
(magic/dunder methods list)
add,sub,mult,matmult,div,truediv,mod,floordiv,divmod,pow,lshift,rshift,and,or,xor
'''