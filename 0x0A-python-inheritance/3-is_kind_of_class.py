#!/usr/bin/python3
"""
Checks if an object is an instance of a specifici class
or a class that was inherited
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an obj is an instance of a specific class

    Args:
        obj: object
        a_class: specific class or class inherited

    Returns:
        True if it's an instance or False if it's not
    """
    return isinstance(obj, a_class)
