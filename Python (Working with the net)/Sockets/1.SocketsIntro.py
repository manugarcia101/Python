# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 19:46:30 2018
@author: Manu
"""

#! Python 3.6.5
#Author: Manuel Garcia Lopez

#sockets intro
import socket

#we are going to use tcp protocol for this connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(s)

server = 'pythonprogramming.net'
port = 80 

server_ip = socket.gethostbyname(server)
print(server_ip)

request = "GET / HTTP/1.1\nHost: "+server+"\n\n"

s.connect((server, port))
s.send(request.encode())
result = s.recv(4096)

#print(result)

while (len(result) > 0):
    print(result)
    result = s.recv(1024)