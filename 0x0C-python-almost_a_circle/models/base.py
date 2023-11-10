#!/usr/bin/python3
"""Defines a class Base"""

import json


class Base:
    """
    A base class with one private class attribute and
    one instance attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialises once an instance is created"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
