# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 13:45:14 2024

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
item_to_find = input("write item to find in shopping list:")
found_at = None
# None is a constant that is used to show that something doesn't have
# for index in range(6):
for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
        # found_at = shopping_list.index(item_to_find)
        break
else:
    print("{} not found".format(item_to_find))

print("Item found at position {}".format(found_at))
