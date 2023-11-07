#!/usr/bin/python3
"""Defines writing to a file"""


def write_file(filename="", text=""):
    """
    writes to a text file

    Args:
        filename: name of file to write to
        text: text

    Returns:
        the number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as data_file:
        return data_file.write(text)
