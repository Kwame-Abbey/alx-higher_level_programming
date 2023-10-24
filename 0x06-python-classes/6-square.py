#!/usr/bin/python3
"""Defines a square"""


class Square:
    """Defines a blueprint for squares"""

    def __init__(self, size=0, position=(0, 0)):
        """magic function that initializes once an instance is created"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """get the value of size"""
        return self.__size

    @property
    def position(self):
        """gets the value of position"""
        return self.__position

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

    @position.setter
    def position(self, value):
        """sets the value of position after verifying certain conditions"""
        for i in range(2):
            if type(value[i]) is not int:
                raise TypeError('position must be a tuple of 2'
                                'positive integers')
            else:
                if value[i] < 0:
                    raise TypeError('position must be a tuple of 2'
                                    'positive integers')
        self.__position = value

    def area(self):
        """returns current square area"""
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print("")
            return
        for i in range(self.position[1]):
            print("")
        for i in range(self.__size):
            print("{}{}".format(" " * self.__position[0], "#" * self.__size))
