# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 12:30:01 2024

@author: Archik
"""


answer = 5
print("Please guess the number between 1 and 10:")
guess = int(input())

if guess != answer:
    if guess < answer:
        print("Please guess higher")
    else:
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done you guessed it")
    else:
        print("Sorry you have not guessed correctly")
else:
    print("You got it the first time")
