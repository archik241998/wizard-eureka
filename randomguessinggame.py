# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 14:11:10 2024.

@author: Archik
"""

import random
answer = random.randint(1, 10)
highest = 10
answer = random.randint(1, highest)
print("Please guess number between 1 and {}: ".format(highest))
i = int(input())
while i != answer:
    if i > answer:
        print("Please guess lower")
        i = int(input())
    elif i == 0:
        break
    else:
        print("Please guess higher")
        i = int(input())
if i == answer:
    print("You guessed correctly")
