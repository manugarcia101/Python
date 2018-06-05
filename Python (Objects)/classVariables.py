# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 10:25:43 2018

@author: UJA
"""
#! Python 3.6.3
#Author: Manuel Garcia Lopez

#Class variables
#We are going to start from the basic employee
#class we did in the classes.py file

class Employee:
    
    #class variables for Employee
    raise_amount = 1.01
    numEmp = 0
    
    #constructor 
    def __init__(self, first, last, pay): 
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '_' + last +'@gmail.com'
        
        Employee.numEmp += 1
        
    #class methods
    #remember always to use self as parameter
    def fullname(self):
        return print('{} {}'.format(self.first, self.last))
    
    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)
        
    #till here so far we have seen how to declare regular methods
    #but let say we want to define a special method class in that case we will do this:
    @classmethod
    def set_raise_amount(cls,amount): #cls is going to be our class vairable name
        #this will change the raise_amount of the class Employee
        cls.raise_amount = amount
        
    '''
    To sum up:
    Class methods are methods that automatically take the class as the first argument. 
    Class methods can also be used as alternative constructors. Static methods do not 
    take the instance or the class as the first argument. They behave just like normal 
    functions, yet they should have some logical connection to our class. 
    '''
    
#Filling the employees with the constructor by parameters        
emp_1 = Employee('Corey','Schafer',900)
emp_2 = Employee('Manu','Garcia',1000)

Employee.set_raise_amount(1.05)
#this is the same as:
Employee.raise_amount = 1.05

#we can see what a class or object contains by doing this:
print(Employee.__dict__)
print(emp_1.__dict__)

'''
we can define anyway more variables for each instance of the class, 
for example: 
we could do: emp_1.raise_amount = 1.05 
and this will be creating a variable for itself with that value, so 
in case that in apply_raise() we have done this:
self.pay = int(self.pay * self.raise_amount)
it would have used its own variable
'''

#some calculations
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
print(Employee.raise_amount)