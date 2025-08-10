# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 21:30:32 2024

@author: Archik
"""
menu = [
      ["eggs", "beans"],
      ["eggs", "sausage", "bean"],
      ["eggs", "spam"],
      ["eggs", "beans", "spam"],
      ["eggs", "beans", "sausage", "spam"],
      ["spam", "beans", "sausage", "spam"],
      ["spam", "eggs", "spam", "spam", "beans", "spam"],
      ["spam", "sausage", "spam", "beans", "spam", "tomato", "spam"],
]

for meal in menu:
    for i in range(len(meal)-1, -1, -1):
        if meal[i] == "spam":
            del meal[i]
    print(meal)
