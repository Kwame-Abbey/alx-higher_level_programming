#!/usr/bin/python3
"""Defines a function for adding two integers"""


def add_integer(a, b=98):
    """
    Computes and return the sum of two numbers

    Args:
        a: first number
        b: second number

    Returns:
        the sum of the two numbers
    """
    if type(a) is float:
        a = int(a)

    if type(b) is float:
        b = int(b)

    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be an integer')

    if type(b) is not int and type(b) is not float:
        raise TypeError('b must be an integer')

    return a + b
