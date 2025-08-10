# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 14:20:43 2024

@author: Archik
"""

numbers = [1, 45, 31, 16, 12, 60,]
for number in numbers:
    if number % 8 == 0:
        # reject the list
        print("The numbers are unacceptable")
        break
else:
    print("All these numbers are fine")
