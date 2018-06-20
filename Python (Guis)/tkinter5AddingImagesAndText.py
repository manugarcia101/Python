# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 10:25:49 2018

@author: Manu
"""

#! Python 3.6.3
#Author: Manuel Garcia Lopez

from tkinter import *

from PIL import Image, ImageTk

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
        
        #quitButton = Button(self, text = 'Quit', command = self.client_exit)
        #tkinter function
        
        #quitButton.place(x = 0, y = 0)
        
        #added menu
        menu = Menu(self.master)
        self.master.config(menu=menu)
        
        file = Menu(menu)
        
        file.add_command(label = 'Save')
        file.add_command(label = 'Exit', command = self.client_exit)
        
        menu.add_cascade(label = 'File', menu = file)
        
        edit = Menu(menu)
        edit.add_command(label = 'Show image', command = self.showImg)
        edit.add_command(label = 'Show text', command = self.showTxt)
        menu.add_cascade(label = 'Edit', menu = edit)
        
    def showImg(self):
        load = image.open('image.jpg')
        render = ImageTk.PhotoImage(load)
        
        img = Label(self, image = render)
        img.image = render
        img.place(x=0, y=0)
        
    def showTxt(self):
        text = Label(self, text = 'Hey there good lookin!')
        text.pack()
        
    def client_exit(self):
        sys.exit()#a way not very cool of terminating a programme
        
        
        
        
    
    
        
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