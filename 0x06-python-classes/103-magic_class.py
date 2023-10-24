#!/usr/bin/python3
"""Bytecode for Magic Class"""

import math


class MagicClass:
    """defines a magic class"""

    def __init__(self, radius=0):
        """initialises the moment an instance is created"""
        self.radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        else:
            self.radius = radius

    def area(self):
        """returns the area of a circle"""
        return self.radius ** 2 * math.pi

    def circumference(self):
        """returns the circumference of a circle"""
        return 2 * self.radius * math.pi
