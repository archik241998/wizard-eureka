# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 14:24:31 2024

@author: Archik
"""

print("Please choose your option from list below: ")
print("1 :\t Learn Python")
print("2 :\t Learn Java")
print("3 :\t Go Swimming")
print("4 :\t Have Dinner")
print("5 :\t Go to Bed")
print("0 :\t Exit")
while True:
    choice = input()
    if choice == "0":
        break
    elif choice in "12345":
        print("You chose {}".format(choice))
