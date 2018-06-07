# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 10:25:43 2018

@author: Manu
"""
#! Python 3.6.3
#Author: Manuel Garcia Lopez

#Class variables
#We are going to start from the basic employee
#class we did in the classes.py file

import datetime

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
        
    #classmethods are also a way of making instances of a class as if they were constructors
    @classmethod
    def from_string(cls,emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    #static methods (common methods, no parameters like self or cls)
    #they don't operate on the instance of the class
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
        
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

#Creating new employees from a string
#example arrays with data
str1 = 'John-Doe-700'
str2 = 'Pepe-Collado-1000'
str3 = 'Leonardo-Di_Caprio-2000'

#new employee objects
new_emp = Employee.from_string(str1)

#raising amounts options
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

#working with static methods
my_date = datetime.date(2018,6,5)

print(Employee.is_workday(my_date))