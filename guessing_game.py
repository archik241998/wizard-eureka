# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 12:22:57 2024

@author: Archik
"""

answer = 5
print("Please guess the number between 1 and 10:")
guess = int(input())
if guess < answer:
    print("Please guess higher")
    guess = int(input())
    if guess == answer:
        print("Well done you guessed it")
elif guess > answer:
    print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done you guessed it")
else:
    print("You got it the first time")
