# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 12:49:34 2024

@author: Archik
"""

if 0:
    print("True")
else:
    print("False")
name = input("Please enter your name: ")
if name != "":
    print("Hello, {}".format(name))
else:
    print("Are you the man with no name")
# in not in
parrot = "Norwegian blue"
letter = input("Enter a character: ")
if letter in parrot:
    print("{} is in {}".format(letter, parrot))
else:
    print("I don't need that letter")
print()
activity = input("What would you like to do today?\n")
if "cinema" not in activity:
    print("But I want to go to cinema")
