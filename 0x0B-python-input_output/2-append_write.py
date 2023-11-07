#!/usr/bin/python3
"""Defines appending text to a file"""


def append_write(filename="", text=""):
    """
    appends text to a file

    Args:
        filename: name of file to write to
        text: text

    Returns:
        the number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as data_file:
        return data_file.write(text)
