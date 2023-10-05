#!/usr/bin/python3
from magic_calculation_102 import add, sub


def magic_calculation(a, b):
    """returns the sum or difference"""
    add = None
    sub = None
    c = None

    if a < b:
        add = globals()['add']
        c = add(a, b)

        for i in range(4, 7):
            c = add(c, i)

        return c
    else:
        return sub(a, b)
