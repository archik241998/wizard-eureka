# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 01:27:46 2024.

@author: Archik
"""


def squareit(x: float) -> float:
    """Get square of a number."""
    return x * x


print(squareit(2))


def dosomething(f, x):
    """
    Get any function to do their work.

    'Args':
        f: Function to work.
        x: Parameter of the function.

    'Returns':
        Result of the function performed on parameter x.

    """
    return f(x)


print(dosomething(squareit, 3))

# Lambda function, let us use inline implification
print(dosomething(lambda x: x * x * x, 3))
