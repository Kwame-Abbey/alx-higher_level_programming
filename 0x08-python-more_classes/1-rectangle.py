#!/usr/bin/python3
"""Defines a rectangle"""


class Rectangle:
    """A rectangle class with two private instance attributes"""

    def __init__(self, width=0, height=0):
        """
        Initializes once an instance is created

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieves the width of the rectangle

        Returns:
            the width of rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Modifies the width according to some conditions

        Args:
            value: value of width
        """
        if type(value) is int:
            if value < 0:
                raise ValueError('width must be >= 0')
            else:
                self.__width = value
        else:
            raise TypeError('width must be an integer')

    @property
    def height(self):
        """
        Retrieves the height of rectangle

        Returns:
            the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Modifies the height on certain conditions

        Args:
            value: value of height
        """
        if type(value) is int:
            if value < 0:
                raise ValueError('height must be >= 0')
            else:
                self.__height = value
        else:
            raise TypeError('height must be an integer')
