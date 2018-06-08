# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 10:30:13 2018

@author: Manu
"""

#! Python 3.6.3
#Author: Manuel Garcia Lopez

#OS Module 
#OS management of directories
import os

#getting the current working directory
currentDir = os.getcwd()
print(currentDir)

#creating a new directory
os.mkdir('newDir2')

import time
time.sleep(2)

#renaming dir names
os.rename('newDir2','newDir3')

time.sleep(2)
#deleting dir
os.rmdir('newDir3')

#we can also extract data help
#help(os)

