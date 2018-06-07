# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 19:13:35 2018

@author: Manu
"""
#! Python 3.6.3
#Author: Manuel Garcia Lopez

#Inheritance and subclasses

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
        return print('{} {}'.format(self.first, self.last))
    
    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)
  
'''
Subclasses: just by inheriting classes, each subclass will
have the same variables and methods as the superclass by default
'''
class Developer(Employee):
    #for example let's say we want to change the raise_amouny of developers
    raise_amount = 1.10
    
    #constructor of the subclass
    def __init__(self, first, last, pay, plang): 
        #call to the super class constructor
        super().__init__(first, last, pay)
        self.plang = plang

class Manager(Employee):
    
    #constructor of the subclass, (employees is a list)
    def __init__(self, first, last, pay, employees=None): 
        #call to the super class constructor
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
            
    #methods
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
            
    def print_emp(self):
        for emp in self.employees:
            emp.fullname()

#instances    
dev_1 = Developer('Corey','Schafer',900,'Python')
dev_2 = Developer('Manu','Garcia',1000,'Java')

#here there is a function that will allow us to understand the flow 
#that our execution classes have
'''print(help(Developer))'''

'''
print(dev_1.pay)
Developer.apply_raise(dev_1)
print(dev_1.pay)
'''

print(dev_1.plang)
print(dev_2.plang)

manager1 = Manager('Sue','Smith',3000,[dev_1])

print(manager1.email)
manager1.print_emp()
manager1.add_emp(dev_2)
print("\n")
manager1.print_emp()
manager1.remove_emp(dev_1)
print("\n")
manager1.print_emp()

'''
lastly, we could use in case we are lost about which object
belongs to each instance, the method isinstance(obj,class)
That will return true, in case it belongs to the class of to 
some subclass of it, otherwise it returns false
'''
print(isinstance(manager1,Developer))#returns false
print(isinstance(manager1,Manager))#returns true
print(isinstance(manager1,Employee))#returns true

'''
the same functionability is use to indentfy classes
and their inheritance with the function issubclass and 
two classes
'''
print(issubclass(Manager,Employee))#returns true
print(issubclass(Manager,Developer))#returns false

'''
Finally let's remark the importance of some libraries as 
the WSGI library app to render default error in a nice way
Also take a look to HTTPException error classes
This is cool in case you don't want to make your own class of errors
'''