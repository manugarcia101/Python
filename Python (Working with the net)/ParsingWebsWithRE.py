# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 13:51:31 2018

@author: Manu
"""

#!Python 3.6.3
#Author: Manuel García López

#regular expressions for parsing websites

import urllib.request
import urllib.parse
import re

url = 'http://pythonprogramming.net'
values = {'s':'basics','submit':'search'}
data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url,data)
resp = urllib.request.urlopen(req)
respData = resp.read()

#print(respData) 

#we are going to search specific info between paragraph texts
#a good combination with re for doing this is: .*? which means
#find me everything
paragraphs= re.findall(r'<p>(.*?)</p>',str(respData))

for eachP in paragraphs:
    print(eachP)