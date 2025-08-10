# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 14:56:01 2024

@author: Archik
"""

result = True
another_result = result
print(id(result))
print(id(another_result))

result = False
print(id(result))
