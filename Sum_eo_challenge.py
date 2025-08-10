# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 20:34:53 2024.

@author: Archik
"""


def sum_eo(n: int, t: str) -> int:
    """
    Get a process of summation of series of `int`.

    This function gives summation of series of odd and even
    numbers, starting from 0. Whether the sum is to be of
    odd numbers or even numbers is to be mentioned in variable
    `t` in `string` format.

    'Args':
        n (int):
                It is the final range of till the series have
                to be summed. This integer itself is not counted among
                the series when being summed. It has to be a positve integer.

        t (str):
                It describes the nature of summation, that is,
                whether the sum is of even numbers `e` or odd numbers `o`.
    -------------------------------------

    'Returns':
        Returns integer -1 for invalid value of `t`.
    --------------------------------------

    """
    while True:
        if t == "e":
            return sum(range(0, n, 2))
        elif t == "o":
            return sum(range(1, n, 2))
        else:
            return -1


print(sum_eo(10, "j"))
