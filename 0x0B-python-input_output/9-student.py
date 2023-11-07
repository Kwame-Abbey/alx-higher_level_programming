#!/usr/bin/python3
"""Defines a class Student"""


class Student:
    """
    A student class with 3 public instance attributes and
    one public method
    """

    def __init__(self, first_name, last_name, age):
        """initialises once an instance is created"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns string representation"""
        return self.__dict__
