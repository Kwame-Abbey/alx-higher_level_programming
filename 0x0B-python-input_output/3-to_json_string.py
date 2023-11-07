#!/usr/bin/python3
"""Defines serializing with json module"""

import json


def to_json_string(my_obj):
    """
    serializes data hierachies with json

    Args:
        obj: data object to be serialized
    """
    return json.dumps(my_obj)
