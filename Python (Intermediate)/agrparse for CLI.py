# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 19:01:44 2018

@author: Manu
"""

#agrparse for CLI, it's an argument parser for the command line
#it is a nice way of working, every time we need to execute smth 
#from command line
import argparse 
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type = float, default = 1.0,
                        help = 'What is the first number?')
    parser.add_argument('--y', type = float, default = 1.0,
                        help = 'What is the first number?')
    parser.add_argument('--operation', type = str, default = 'add',
                        help = 'What operation()? (add,sub,mul,div)')
    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))

def calc(args):
    if args.operation == 'add':
        return args.x + args.y
    elif args.operation == 'sub':
        return args.x - args.y
    elif args.operation == 'mul':
        return args.x * args.y
    elif args.operation == 'div':
        return args.x / args.y
    
#it is a good practice to do this when we have a main func
#just to ensure we are running the correct one
if __name__== '__main__':
    main()

'''
running this by default it will just give us 2.0, but we can 
send different args in command line as: --x=4 --y=8 --operation=mul
To get the help output we have to (in command line) write -h
'''
