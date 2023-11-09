#!/usr/bin/python3
"""Defines a square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """A square class that inherits a rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialises once an instance of square is created"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Readable string representation"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}" \
            .format(self.id, self.x, self.y, self.width)
