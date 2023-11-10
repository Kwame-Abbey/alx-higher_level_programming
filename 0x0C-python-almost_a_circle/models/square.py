#!/usr/bin/python3
"""Defines a square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """A square class that inherits a rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialises once an instance of square is created"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Retrieves value of size"""
        return self.width

    @size.setter
    def size(self, value):
        """Modifies value of size"""
        self.width = value
        self.height = value

    def __str__(self):
        """Readable string representation"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}" \
            .format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """assigns attributes"""
        if len(args) != 0:
            square_attr = ['id', 'size', 'x', 'y']
            i = 0

            for arg in args:
                setattr(self, square_attr[i], arg)
                i += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
