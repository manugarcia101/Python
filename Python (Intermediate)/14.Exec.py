# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 18:44:30 2018

@author: Manu
"""

#!Python 3.6.5
#Author: Manuel García López

#Exec in python (compiling in python)
exec("print('so this works like eval')")

list_str = "[2,3,5,4]"
list_str = exec(list_str)

print(list_str)#it returns the action of that(None)

exec("list_str2 = [2,3,5,4,1]")
print(list_str2)

exec("def test(): print('oh my gosh')")
test()

exec("""
def test2():
    print('pretty cool')
""")
test2()