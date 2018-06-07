# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 09:36:52 2018

@author: Manu
"""

#! Python 3.6.3
#Author: Manuel Garcia Lopez

#Reading data from a CSV
#first we have to import the csv library
import csv

#in this case we open a already existing csv
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
    
    wColor = input('What color do you wish to know the date of?')
    coldex = colors.index(wColor)
    
    theDate = dates[coldex]
    
    print('The date of ',wColor,' is: ',theDate)
    
#writing to a CSV
#we have to create a csv in writting mode
with open('example2.csv','w',newline='') as f:
    fieldnames = ['column1','column2','column3']
    writer = csv.DictWriter(f,fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerow({'column1':'one','column2':'two','column3':'three'})
        
    