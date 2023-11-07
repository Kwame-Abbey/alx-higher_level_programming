#!/usr/bin/python3
"""Reads from a file"""


def read_file(filename=""):
    """
    Reads a text file and prints it to stdout

    Args:
        filename: name of file to read
    """
    with open(filename, 'r', encoding='utf-8') as data_file:
        contents = data_file.read()
        print(contents, end='')
