# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 10:37:12 2018

@author: Manu
"""
#! Python 3.6.5
#Author: Manuel Garcia Lopez

#ftplib
from ftplib import FTP

ftp = FTP('domainname.com')
ftp.login(user='username', passwd='password')
ftp.cwd('/specificdomain-or-location/')

def grabFile():
    fileName = 'fileName.txt'
    localfile = open(filename, 'wb')
    ftp.retrbinary('RETR' + filename, localfile.write, 1024)
    ftp.quit()
    localfile.close()
    
def placeFile():
    filename = 'fileName.txt'
    ftp.storbinary('STOR' + filename, open(filename, 'rb'))
    ftp.quit()