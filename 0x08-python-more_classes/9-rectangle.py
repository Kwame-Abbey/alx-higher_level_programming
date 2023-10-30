#!/usr/bin/python3
"""Defines a rectangle"""


class Rectangle:
    """A rectangle class with two private instance attributes"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initializes once an instance is created

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    def __str__(self):
        """print the string representation of the rectangle"""
        string = ""
        if self.width == 0 or self.height == 0:
            return string
        for i in range(self.height):
            string += Rectangle.print_symbol * self.width
            if i < self.height - 1:
                string += "\n"
        return string

    def __repr__(self):
        """ returns developer's version of rectangle """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

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

    def area(self):
        """
        computes the area of the rectangle

        Returns:
             the area of rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Computes the perimeter of rectangle

        Returns:
             the perimeter of rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)

    def __del__(self):
        """ prints message when an instance is deleted """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ returns rectangle with largest area """
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if isinstance(rect_2, Rectangle) is False:
            raise TypeError('rect_2 must be an instance of Rectangle')
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        """ returns new rectangle instance that is a square """
        return cls(size, size)
