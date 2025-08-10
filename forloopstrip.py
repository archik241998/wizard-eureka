# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 13:15:04 2024

@author: Archik
"""

number = "9,233,327,036,854,775,887"
# input("Please enter a series of number using any separator you like = ")
separator = ", "
for char in number:
    if not char.isnumeric():
        separator = separator + char
print(separator)
values = "".join(char if char not in separator else " "
                 for char in number).split()
print(values)
print(sum(int(val) for val in values))
