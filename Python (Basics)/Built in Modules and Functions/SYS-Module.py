# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 10:47:28 2018

@author: Manu
"""

#! Python 3.6.3
#Author: Manuel Garcia Lopez

#SYS Module 
#system operations management module lib
import sys

#output text with color
sys.stderr.write('This is stderr test')
sys.stderr.flush()
sys.stdout.write('This is stdout test')

#file path routing
print(sys.argv)

#playing with the argument passing
if len(sys.argv) > 1:
    print(sys.argv[1])
    
'''
we have to take into account that python management
systems is really powerful, and it can be combined with 
directory management and act like a bash language, so 
in fact we can do with python, the same as with other 
programming language, the same as with other bash 
language and also, we will see that in the future, 
python could be use 
'''