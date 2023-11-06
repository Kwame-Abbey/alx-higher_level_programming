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
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height

    def area(self):
        """
        Computes the area of a rectangle

        Returns:
            the area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        printable string representation of object

        Returns:
            the string representation of object
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
