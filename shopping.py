# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 13:29:32 2024

@author: Archik
"""

shopping_list = [
                "Milk",
                "pasta",
                "Eggs",
                "spam",
                "bread",
                "rice",
                ]
for item in shopping_list:
    print("Buy" + item)
print()
for item in shopping_list:
    if item == "spam":
        continue
    print("Buy" + item)
"""
for item in shopping_list:
    if item != "spam":
        print("Buy" + item)
"""
for item in shopping_list:
    if item == "spam":
        break
    print(item)
