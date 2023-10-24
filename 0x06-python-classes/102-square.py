#!/usr/bin/python3
"""Compares two squares"""


class Square:
    """Defines a blueprint for squares"""

    def __init__(self, size=0):
        """magic function that initializes once an instance is created"""
        self.size = size

    @property
    def size(self):
        """get the value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the value of size after verifying certain conditions"""
        if type(value) is int:
            if value < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = value
        else:
            raise TypeError('size must be an integer')

    def area(self):
        """returns current square area"""
        return self.__size ** 2

    def __eq__(self, other):
        """
        check if square is equal to other square
        """
        return self.size == other.size

    def __ne__(self, other):
        """
        check if square is not equal to other square
        """
        return self.size != other.size

    def __gt__(self, other):
        """
        check if square is greater than other square
        """
        return self.size > other.size

    def __lt__(self, other):
        """
        check if square is less than other square
        """
        return self.size < other.size

    def __ge__(self, other):
        """
        check if square is greater than or equal to other square
        """
        return self.size >= other.size

    def __le__(self, other):
        """
        check if square is less than or equal to other square
        """
        return self.size <= other.size
