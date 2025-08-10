# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 14:59:09 2024

@author: Archik
"""

shopping_list = [
    "milk",
    "pasta",
    "eggs",
    "spam",
    "bread",
    "rice",
    ]
another_list = shopping_list
print(id(shopping_list))
print(id(another_list))
shopping_list = ["cookies"]
print(shopping_list)
print(id(shopping_list))
# binding multiple names to a list
a = b = c = d = e = f = another_list
print(a)
print("Adding cream")
b.append("cream")
print(c)
print(d)
