#!/usr/bin/python3
"""Defines a rectangle"""

from models.base import Base


class Rectangle(Base):
    """A rectangle class that inherits Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialises once an instance is created"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.id = id
        super().__init__(id)

    @property
    def width(self):
        """retrives value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """modifies the value of width"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """retrives value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """modifies the value of height"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """retrives value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """modifies the value of x"""
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """retrives value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """modifies the value of y"""
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """computes area of rectangle"""
        return self.width * self.height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        print("\n" * self.y, end='')
        for i in range(self.height):
            print(f"{' ' * self.x}", end='')
            print(f"{'#' * self.width}")

    def __str__(self):
        """returns the readable string representation"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}" \
            .format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if len(args) != 0:
            rect_attributes = ['id', 'width', 'height', 'x', 'y']
            i = 0

            for arg in args:
                setattr(self, rect_attributes[i], args[i])
                i += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ returns the dictionary representation of a Rectangle"""
        rect_attributes = ['id', 'width', 'height', 'x', 'y']
        rect_dict = {}
        for attr in rect_attributes:
            rect_dict[attr] = getattr(self, attr)
        return rect_dict
