# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 10:44:48 2018

@author: Manu
"""

#! Python 3.6.3
#Author: Manuel Garcia Lopez

from tkinter import *

class Window(Frame):
   
    #main class init
    def __init__(self, master = None):
        Frame.__init__(self, master)
        
        self.master = master
        
root = Tk()#tkinter function

app = Window(root)

root.mainloop()