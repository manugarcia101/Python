# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 19:03:46 2018

@author: Manu
"""

#!Python 3.6.5
#Author: Manuel García López

#Threading module

import threading 
from queue import Queue
import time

'''
The idea of threading is that once we have multiple tasks, 
it could be a good idea to make the running process faster
by dividing those tasks into some execution threads, but we 
will have to face the problem of variables information sharing,
to deal with that we will use locks (mutex critical sections)
'''

print_lock = threading.Lock()

def exampleJob(worker):
    time.sleep(0.5)
    
    with print_lock:
        print(threading.current_thread().name, worker)
        
def threader():
    while True:
        worker = q.get()
        exampleJob(worker)
        q.task_done()#thread completed, we are ready to move on
        

q = Queue()

for x in range(10):
    t = threading.Thread(target = threader)
    t.daemon = True
    t.start()
    
start = time.time()

for worker in range(20):
    q.put(worker)
    
q.join()#we wait until the thread finishes

print('Entire job took: ',time.time()-start)