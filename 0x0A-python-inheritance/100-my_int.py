#!/usr/bin/python3
"""Defines inherited of int"""


class MyInt(int):
    """MyInt class that inherits int"""

    def __eq__(self, other):
        """compares self and other value"""
        return int.__ne__(self, other)

    def __ne__(self, other):
        """compares self and other value"""
        return int.__eq__(self, other)
