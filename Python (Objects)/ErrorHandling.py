# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 11:09:02 2018

@author: Manu
"""

#! Python 3.6.3
#Author: Manuel Garcia Lopez

#Try and Except error handling
#we are gonna use the same code as for reading the csv
import csv

with open('example.csv') as csvFile:
    #we can save the data spliting by comas
    readCSV = csv.reader(csvFile, delimiter = ',')
    print(readCSV)
    
    dates = []
    colors = []
    
    for row in readCSV:
        dates.append(row[0])
        colors.append(row[4])
    
    print(dates)
    print(colors)
    
    '''
    Exceptions should be used just in case of extremely neccesity, 
    if we can avoid them, just avoid them, by if/else statement
    or whatever
    It's important to be as clear as possible when throwing an 
    exception
    '''
    
    try:
        wColor = input('What color do you wish to know the date of?')
        coldex = colors.index(wColor)
        
        theDate = dates[coldex]
        
        print('The date of ',wColor,' is: ',theDate)

    # General exception handling
    # except Exception, e: Python 2.7
    except Exception as e: #Python 3.smth
        print(e)
        
    #To be more specific in exception handling, we can use 
    #predefined exceptions as: NameError
        
    print('continuing')
        