# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 12:35:53 2024

@author: Archik
"""

age = int(input("How old are you ?"))
if age >= 16 and age <= 65:
    print("Have a good day at work")
else:
    print("Enjoy your free time")
print("-" * 80)
print()
if age < 16 or age > 65:
    print("Enjoy your free time")
else:
    print("Have a great day at work")
