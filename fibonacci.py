# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 18:36:42 2024.

@author: Archik
"""


def fibonacci(n: int) -> int:
    """
    Return `n` th fibonacci series for positive `n`.

    'Args':
        n : Must be a positive integer.
    ---------------

    'Returns':
        `n` th fibonacci number.
    ---------------

    """
    if 0 <= n <= 1:
        return n
    n_minus1, n_minus2, result = 1, 0, None
    for f in range(n - 1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result
    return result


for i in range(36):
    print(i, fibonacci(i))
