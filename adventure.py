# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 14:00:53 2024

@author: Archik
"""

available_exits = ["North", "South", "East", "West"]
chosen_exit = ""
# while chosen_exit not in available_exits:
#     chosen_exit = input("Please choose a direction: ")
# print("Aren't you glad you got out of there")

while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction: ")
    if chosen_exit.casefold() == "quit":
        print("Gameover")
        break
print("Aren't you glad you got out of there")
