# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 12:59:26 2023

@author: Archik
"""

answer=5
print("Please guess the number between 1 and 10:")
guess=int(input())
#if guess<answer:
#   print("Please guess higher")
  #  guess=int(input())
   # if guess==answer:
    #    print("Welldone! you guessed right")
#elif guess>answer:
#    print("Please guess lower")
 #   guess=int(input())
  #  if guess==answer:
   #     print("Welldone! you guessed right")
#else:
    #print("You got it the first time")
if guess==answer:
    print("You got it the first time")
    
else:
    if guess<answer:
        print("Please guess higher")
    else: #Guess must be greater than answer
        print("Please guess lower")
    guess=int(input())
    if guess==answer:
        print("Welldone! you guessed right")
    else:
        print("Sorry, you havenot guessed right")
    
