# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 11:14:48 2018

@author: Manu
"""

#! Python 3.6.5
#Author: Manuel Garcia Lopez

#simplePortSocketScanner
import socket

#we are going to use tcp protocol for this connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = 'pythonprogramming.net'

def pscan(port):
    try:
        s.connect((server, port))
        return True
    except:
        return False
    
for x in range(1,26):
    if pscan(x):
        print('Port',x,'is open!!!!!!!')
    else:
        print('Port',x,'is closed')
        
        