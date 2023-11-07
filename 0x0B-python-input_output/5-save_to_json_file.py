#!/usr/bin/python3
"""Defines writing to a text file using JSON representation"""

import json


def save_to_json_file(my_obj, filename):
    """
    writes an object to a text file using JSON

    Args:
        my_obj: object
        filename: file object
    """
    with open(filename, 'w', encoding='utf-8') as data_file:
        json.dump(my_obj, data_file)
