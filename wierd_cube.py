# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 22:20:02 2024.

@author: Archik
"""


def pinreverse(n: int, m: int) -> int:
    """
    Print `int` in reverse order.

    'Args':
        n (int): n in reverse order.
        m (int): m last number in series
    ----------------

    """
    i = n
    j = m
    while i >= j:
        print(m, end="" * i)
        i -= 1
        m += 1


# pinreverse(25, 20)
print()


def reverse_print(n: int) -> int:
    """Print the digits of an integer in reverse order."""
    while n > 0:
        digit = n % 10
        print(digit, end="")
        n //= 10


def wierd_square(n: int, m: int):
    """
    Create a weired spiral square in reverse.

    Square of number in reverse counting

    'Args':
        n: Number of rows.
        m: Number of columns.
    -----------------------

    'Returns':
        None.
    -----------------------

    """
    k = 0
    for i in range(1, n + 1):
        print()
        for j in range(1, m + 1):
            if i == 1:
                sq = str((m * n) - k).ljust(2)
                print(sq, end=" ")
                k += 1
            else:
                sq = str((m + n) - (j)).ljust(2)
                print(sq, end=" ")
                k += 1


wierd_square(3, 3)
