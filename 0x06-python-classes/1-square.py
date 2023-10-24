#!/usr/bin/python3
"""Defines a square"""


class Square:
    """Defines a square class with private instance attribute size"""

    def __init__(self, size):
        """magic function that initializes once an instance is created"""
        self.__size = size
