# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 13:03:07 2024

@author: Archik
"""

name = input("Please enter your name: ")
age = int(input("How old are you? \n"))
if 18 <= age <= 31:
    print("Welcome to club 1830 holidays, {}".format(name))
else:
    print("I am sorry, our holiday is only for cool people")
