# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 18:28:53 2018

@author: Manu
"""

#! Python 3.6.3
#Author: Manuel Garcia Lopez

#writing to file
text = "Sample text\nNew line of text"

'''
we are going to save this text variable in a txt called exampleFile
if it doesn't exist, it is going to be created
w in the open function parameters means it is going to override
whatever was previously written in the file (if it exists)
'''
saveFile = open("exampleFile.txt","w")
saveFile.write(text)
saveFile.close()#for security (to avoid memory leaks), 
                #always close the file

#reading from file
readFile = open("exampleFile.txt","r")
print(readFile.name)
print(readFile.mode)#shows mode of file (w,r or r+) for writing, 
                    #reading or reading and writing

readFile.close()

#reading and writing files
readWriteFile = open("exampleFile.txt","r+")

readWriteFile.close()

#Append files
appendMe = "\nNew line appended"
appendFile = open("exampleFile.txt","a") #a means not to override the current data
appendFile.write(appendMe)
appendFile.close()

'''
for now so far this has been the common way of working with files
now we are going to work in a different way, with content managers
'''

with open("exampleFile.txt","r") as file:
    readingSize = 20
    contents = file.read() #shows all the text
    contents = file.read(readingSize) #gets first 20 characters 
    contents2 = file.readlines() #shows everything in a single line
    contents3 = file.readline() #shows the first line
    print(contents3, end='')#end removes a white extra line
    
    file.seek(0) #seek function allows you to put the reading pointer
                #at the position passed by parameter
    
    print(file.tell()) #shows you the current position (in chars) of the file
                        #you are reading
    
    #but readlines several times is not funny, instead better using loops
    for line in file:
        print(line, end='')
        
    while len(contents) > 0:
        print(contents, end='')
        contents = file.read(readingSize)
        
with open("exampleFile2.txt","w") as file:

    file.write("testing this file") 
    '''
    variable.write("smth") writes smth where the writing pointer
    is pointing to, in case the file is just opened, it points
    to the first char pos (0)
    '''
    file.seek(0)
    '''
    file.seek(number) points the writing pointer to where you
    specified by number and overrides what was previously there
    '''

#making copies of a file
with open("exampleFile.txt","r") as readFile:
    with open("exampleCopy.txt","w") as writeFile:
        for line in readFile:
            writeFile.write(line)
            
#making copies of other objects, let's say for example, an image
#this is done in binary mode (rb,wb,rb+)
with open("image.jpg","rb") as readFile:
    with open("imageCopy.jpg","wb") as writeFile:
        for line in readFile:
            writeFile.write(line)

#but, what about copying data instead of files? Let's see how
with open("image.jpg","rb") as readFile:
    with open("imageCopy.jpg","wb") as writeFile:
        #we can create a variable of a set size to copy just the 
        #exact amount of data we want
        chunk_size = 4096
        readFile_chunk = readFile.read(chunk_size)
        while len(readFile_chunk) > 0:
            writeFile.write(readFile_chunk)
            readFile_chunk = readFile.read(chunk_size)
            
