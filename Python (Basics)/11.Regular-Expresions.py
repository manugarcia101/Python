# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 13:32:23 2018

@author: Manu
"""

#!Python 3.6.3
#Author: Manuel García López

#Regular expresions
'''
A regular expression, regex or regexp (sometimes called 
a rational expression) is, in theoretical computer science 
and formal language theory, a sequence of characters that 
define a search pattern. Usually this pattern is then used 
by string searching algorithms for "find" or "find and replace" 
operations on strings, or for input validation.
'''

'''
Identifiers:
\d any number
\D anything but a number
\s space 
\S anything but a space
\w a character
\W anything but a character
.  any character, except for a newline
\b the whitespac around words
\. a period

Modifiers:
{1,3} we are expecting 1-3, example: \d{1-3}
+  Match 1 or more
?  Match 0 or 1
*  Match 0 or more
$  Match the end of a string
^  Match the beginning of a string
|  Match either or, example: \d{1-3} | \w{5-6}
[] Range or "variance", example: [A-Z] or [1-5a-qA-Z]
{x} Expecting x amount

White Space Characters:
\n new line
\s space
\t tab
\e escape
\f form feed
\r return

DONT FORGET!:
. + * ? [ ] $ ^ ( ) { } | \
'''
#we are going to make an import of regular expresions lib
import re

#we are going to make a new string, and we are going to search
#some special data by using re 
exString = '''
Jessica is 15 years old, and Daniel is 27 years old.
Edward is 67, and his grandfather, Oscar, is 102.
'''

#we ask for finding the possible age: 1-3 chars
ages = re.findall(r'\d{1,3}',exString)
#we ask for finding the possible names: 1-3 chars
names = re.findall(r'[A-Z][a-z]*',exString)

print(ages)
print(names)

ageDict = {}

x = 0
for eachName in names:
    ageDict[eachName] = ages[x]
    x+=1

print(ageDict)