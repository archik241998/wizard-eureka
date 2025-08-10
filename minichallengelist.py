# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 22:32:53 2024

@author: Archik
"""
value_list = ['9', '223', '372', '036', '854', '775', '807']
sep = ","
for i in range(len(value_list)-1, -1, -1):
    if i != sep:
        value_list[i] = int(value_list[i])
print(value_list)
#num = " ".join((n for n in value_list)).split(',')
#print(int(num))