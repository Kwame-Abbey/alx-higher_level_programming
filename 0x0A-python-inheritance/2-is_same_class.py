#!/usr/bin/python3
"""Checks if an object is an instance of a specific class"""


def is_same_class(obj, a_class):
    """
    Checks if an obj is an instance of a specific class

    Args:
        obj: object
        a_class: specific class

    Returns:
        True if it's an instance or False if it's not
    """
    return type(obj) == a_class
