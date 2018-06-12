# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 20:04:43 2018

@author: Manu
"""

#!Python 3.6.3
#Author: Manuel García López

#Multiprocessing
'''
Why multiprocessing when we have several cores in our CPU's?
Because of the security lock of our computers.
What does multiprocessing allows?
To run several processes at the same time in different cores
'''

import multiprocessing

def spawn(num, num2):
    print('Spawned! {} {}'.format(num, num2))
    '''
    if join is not set, they will be executed asynchronously,
    if join is set, they will be executed in order
    '''
    
if __name__ == '__main__':
    for i in range(50):
        p = multiprocessing.Process(target = spawn, args=(i,i+1))
        p.start()
        #p.join()#this wait for other processes to run, 
                #if we commented it we will have more processes
                #running on the cpu
        