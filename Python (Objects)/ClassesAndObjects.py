# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 19:46:30 2018

@author: Manu
"""

#! Python 3.6.3
#Author: Manuel Garcia Lopez

#Classes in Python
#Basic class example with some easy methods
class calculator:
    
    def addition(x,y):
        added = x + y
        print(added)
    
    def substraction(x,y):
        sub = x - y
        print(sub)
        
    def multiplication(x,y):
        mult = x*y
        print(mult)
        
    def division(x,y):
        div = x/y
        print(div)
        
#call to the class methods
calculator.addition(3,7)
calculator.substraction(3,7)
calculator.multiplication(3,7)
calculator.division(3,7)

#another class more complex
class Employee:
    
    def __init__(self, first, last, pay):#constructor 
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '_' + last +'@gmail.com'
        
    #class methods
    def fullname(self):
        return print('{} {}'.format(self.first, self.last))

#Filling the employees with the constructor by parameters        
emp_1 = Employee('Corey','Schafer',900)
emp_2 = Employee('Manu','Garcia',1000)

'''
Filling the employees manually

print(emp_1)
print(emp_2)

emp_1.first = 'Corey'
emp_1.last = 'Schafer'
emp_1.email = 'Corey_Schafer@gmail.com'
emp_1.pay = 900

emp_2.first = 'Manu'
emp_2.last = 'Garcia'
emp_2.email = 'Manu_Garcia@gmail.com'
emp_2.pay = 1000
'''
print(emp_1.email)
print(emp_2.email)

#now without using a method, we are going to show the full object data 
#in a single line
print('{} {}'.format(emp_1.first, emp_1.last))
#or we can use our own created method using the () at the end of the call
#otherwise we just get that our method belongs to x class and the instance and not the result we want
emp_1.fullname()
#by calling the class, the call to that function will look like this
Employee.fullname(emp_1)
