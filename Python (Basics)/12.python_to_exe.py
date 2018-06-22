# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 09:59:33 2018

@author: Manu
"""

#! Python 3.6.5
#Author: Manuel Garcia Lopez

#we are going to use the code of urlib tutorial

import urllib.request #get 
import urllib.parse #parse

x = urllib.request.urlopen('https://www.google.com')

#print(x.read()) #this returns the json response from the http of the url 

url = 'http://pythonprogramming.net' #url pf the web 
dictionary = {'s':'basic','submit':'search'} #we are going to create a dictionary with the basic serach variables the Google use

data = urllib.parse.urlencode(dictionary) #now we encode the dictionary info
data = data.encode('utf-8') #and now we translate it to utf-8
req = urllib.request.Request(url,data) #we need to open a request with the url and the data
resp = urllib.request.urlopen(req) #and then we establish a url with all of that
respData = resp.read() #we read the data and print the response

print(respData)

try: 
    x = urllib.request.urlopen('https://www.google.com/search?q=test')
    
    print(x.read())
    
except Exception as e:
    print(str(e))
    
'''
In this case, we are going to try with an internet server client and we will follow the same steps in order to get
a JSON response from the platform, but this time, saving that info into a plain text file
'''

try:
    url = 'https://www.google.com/search?q=test'
    
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'
    req = urllib.request.Request(url, headers= headers)
    resp = urllib.request.urlopen(req)
    respData = resp.read()
    
    saveFile = open('withHeaders.txt','w')
    saveFile.write(str(respData))
    saveFile.close()

except Exception as e:
    print(str(e))