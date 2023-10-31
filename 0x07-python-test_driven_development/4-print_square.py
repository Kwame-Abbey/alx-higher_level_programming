#!/usr/bin/python3
"""Defines a print square function"""


def print_square(size):
    """
    prints a square with the character #

    Args:
        size: size of side of square
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        print(f"{'#' * size}")
