# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 20:35:57 2018

@author: Manu
"""

#!Python 3.6.3
#Author: Manuel García López

#Getting returned values from processes
from multiprocessing import Pool
#allows us to create a pool of precess forkers

def job(num):
    return num * 2

if __name__ == '__main__':
    p = Pool(processes = 20)
    data = p.map(job, range(20)) #that retrieves 20 vars just in one
    data2 = p.map(job, [5, 4])
    p.close()
    print(data)
    print(data2)
    
