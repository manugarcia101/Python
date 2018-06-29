# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 19:23:23 2018

@author: Manu
"""

#!Python 3.6.5
#Author: Manuel García López

#python pickle module
import pickle #serialization for objs

#exporting to binary file
example_dict = {1:"6",2:"2",3:"1"}

pickle_out = open("dict.pickle","wb")
pickle.dump(example_dict, pickle_out)
pickle_out.close()

#importing from binary file
pickle_in = open("dict.pickle","rb")
example_dict1 = pickle.load(pickle_in)

print("Printing binary file")
print(example_dict1)
print(example_dict1[3])