#!/usr/bin/python3
"""Defines a base geometry"""


class BaseGeometry:
    """A basegeometry class with a public class method area"""

    def __init__(self):
        """Initialises once an instance is created"""
        pass

    def area(self):
        """Raises an Exception"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Validates integer

        Args:
            name: name which is always a string
            value: value
        """
        if type(value) is not int:
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
