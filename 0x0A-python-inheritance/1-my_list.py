#!/usr/bin/python3
"""Prints a sorted list"""


class MyList(list):
    """A child class Mylist that inherits a parent class list"""

    def print_sorted(self):
        """prints the list, but sorted"""
        print(sorted(self))
