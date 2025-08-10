"""Guessing Game with while loop."""
import random


def get_integer(prompt: str) -> int:
    """
    Get an integer from Standard input (stdin).

    The function will continue looping, and prompting
    the user until a valid `int` is entered.

    Args: prompt (any): The string that the user will
            see, when they're prompted to enter the value.
    Returns: The integer that the user enters.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        # else:
        print("invalid input")


highest = random.randint(5, 15)
answer = random.randint(1, highest)
print("Please guess the number between 1 and {0}:".format(highest))
i = get_integer(": ")
if i == answer:
    print("You've guessed it the first time")
else:
    while i != answer:
        if highest > i > answer:
            print("Please guess lower")
            i = int(input())
        elif i > highest or i < 1:
            print("You have guessed outside the limit and broke the game. "
                  "Bye Bye!!")
            break
        else:
            print("Please guess higher")
            i = int(input())
if i == answer:
    print("You've guessed correctly ")
