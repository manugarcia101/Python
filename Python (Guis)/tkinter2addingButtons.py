# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 10:55:47 2018

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
        
        self.init_window()
        
    #specific inti function for our window
    def init_window(self):
        
        self.master.title("GUI")
        
        self.pack(fill = BOTH, expand = 1)
        
        quitButton = Button(self, text = 'Quit')#tkinter function
        
        quitButton.place(x = 0, y = 0)
        
        
        
        
root = Tk()#tkinter function

#now we are going to resize our tkinter window
w = 800 # width for the Tk root
h = 650 # height for the Tk root

# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the screen 
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
app = Window(root)

root.mainloop()