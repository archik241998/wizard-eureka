# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 12:00:18 2024

@author: Archik
"""

for i in range(1, 13):
    print("Number {} squared is {} and cubed is {:4}"
          .format(i, i**2, i**3))
print("*" * 80)
name = input("Please enter your name: ")
age = int(input("How old are you, {0}".format(name)))
print(age)
if (100 >= age >= 18):
    print("You are old enough to vote. Please put an X in the box")
# a colon tells python to expect a new code block
elif age == 900:
    print("Sorry Yoda you died in Return of the Jedi")
else:
    print("Please come back in {0} years".format(18 - age))
print()
if (age < 18):
    print("Please come back in {0} years".format(18 - age))
# a colon tells python to expect a new code block
elif age == 900:
    print("Sorry Yoda you died in Return of the Jedi")
else:
    print("You are old enough to vote. Please put an X in the box")
