#!/usr/bin/python3
"""Defines deserializing with json"""

import json


def from_json_string(my_str):
    """
    deserializes a json string

    Args:
        my_string: json string to deserialize
    """
    return json.loads(my_str)
