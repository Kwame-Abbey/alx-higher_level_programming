#!/usr/bin/python3
"""A class that inherits another class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle class that inherits BaseGeometry"""

    def __init__(self, width, height):
        """
        Initialises once an instance is created

        Args:
            width: width of rectangle
            height: height of rectangle
        """
        if self.integer_validator('width', width):
            self.__width = width
        if self.integer_validator('height', height):
            self.__height = height
