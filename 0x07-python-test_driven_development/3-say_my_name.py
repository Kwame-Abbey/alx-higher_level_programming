#!/usr/bin/python3
"""Prints first name and last name to standard output"""


def say_my_name(first_name, last_name=""):
    """
    Prints concatenated first name and last name

    Args:
        first_name (str): First name
        last_name (str): Last name

    """

    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')

    print(f"My name is {first_name} {last_name}")
