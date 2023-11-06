#!/usr/bin/python3
"""lists all available attributes and methods of an object"""


def lookup(obj):
    """
    lists all attr and methods of an object

    Returns:
        a list of all attributes and methods
    """
    return dir(obj)
