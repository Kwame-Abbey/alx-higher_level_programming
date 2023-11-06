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
