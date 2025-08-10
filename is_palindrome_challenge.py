# -*- coding: utf-8 -*-!
"""
Created on Mon Aug 26 17:05:12 2024.

@author: Archik
"""


def is_palindrome(string: str) -> str:
    """
    Check if a string is a palindrome.

    A palindrome is a string that reads the same forwards as backwards.

    'Args':
        string (str): The string to check.
    --------------

    'Returns':
        True if `string` is a palindrome, False otherwise.
    --------------

    """
    return string[::-1].casefold() == string.casefold()


word = input("Please enter a word to check: ")
if is_palindrome(word):
    print("'{}' is a palindrome".format(word))
else:
    print("'{}' is not a palindrome".format(word))
