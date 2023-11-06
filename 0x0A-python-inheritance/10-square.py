#!/usr/bin/python3
"""Defines a square"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square class that inheirts a rectangle"""

    def __init__(self, size):
        """
        Initialises once an instance is created

        Args:
            size: size of a side of square
        """
        if self.integer_validator('size', size):
            self.__size = size

        super().__init__(size, size)
