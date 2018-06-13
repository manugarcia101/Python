# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 19:05:34 2018

@author: Manu
"""

#!Python 3.6.3
#Author: Manuel García López

#Beautiful soup (scraping and parsing)

#little example of use
import bs4 as bs
import urllib.request

source = urllib.request.urlopen(
        'https://pythonprogramming.net/parsememcparseface/').read()

soup = bs.BeautifulSoup(source, 'lxml')

for paragraph in soup.find_all('p'):
    print(paragraph.text)

print(soup.get_text())

for url in soup.find_all('a'):
    print(url.get('href'))