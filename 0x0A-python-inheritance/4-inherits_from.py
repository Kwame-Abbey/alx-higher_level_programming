#!/usr/bin/python3
"""
Checks if an object is a instance of a class that inherits
(directly or indirectly a specified class)
"""


def inherits_from(obj, a_class):
    """
    Checks if an object is a subclass of a class

    Args:
        obj: object
        a_class: specified class

    Returns:
        True or False
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
