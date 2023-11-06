#!/usr/bin/python3
"""function add_attribute to add attribute if possible"""


def add_attribute(obj, name, value):
    """ if possible, add a new attribute to an object """
    if hasattr(obj, '__dict__'):
        setattr(obj, name, value)
    else:
        raise TypeError('can\'t add new attribute')
