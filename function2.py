# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 18:17:09 2024.

@author: Archik
"""


def multiply(x: float, y: float) -> float:
    """
    Multiply 2 numbers.

    Although this function is intended to multiply 2 numbers,
    you can also use it to multiply a sequence.  If you pass
    a string, for example, as the first argument, you'll get
    the string repeated `y` times as the returned value.

    'Args':
        x : The first number to multiply.
        y : The number to multiply `x` by.
    ----------

    'Returns':
        result (numeric): The product of `x` and `y`.
    ----------

    """
    result = x * y
    return result


answer = multiply(10.5, 4)
print(answer)

answer = multiply(6, 7)
print(answer)
