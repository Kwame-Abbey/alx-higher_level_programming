#!/usr/bin/python3
"""Defines creating am object from a JSON file"""

import json


def load_from_json_file(filename):
    """
    creates an object from a json file

    Args:
        filename: name of file
    """
    with open(filename, 'r', encoding='utf-8') as data_file:
        return json.load(data_file)
