# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 17:24:32 2024.

@author: Archik
"""


def is_palindrome_sentence(sentence: str) -> str:
    """
    Check whether the sentence is a palindrome.

    This function checks whether the mentioned `string`
    input is a palindrome or not. It ignores whitespace,
    capitalisation and punctuation in the sentence.

    'Args':
        sentence (str): It is the string taken as input
        and only alpha-numeric strings are checked for the
        palindrome.
    ----------------

    'Returns':
        It returns `True` if the string checks out to be a
        pallindrome and returns `False` otherwise.
    ----------------

    """
    sword = "".join(char for char in sentence if char.isalnum())
    return sword[::-1].casefold() == sword.casefold()


w = input("Please enter a sentence to check: ")
if is_palindrome_sentence(w):
    print("true")
else:
    print("false")
print(is_palindrome_sentence(w))
