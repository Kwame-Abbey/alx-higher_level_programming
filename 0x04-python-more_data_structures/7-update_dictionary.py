#!/usr/bin/python3


def update_dictionary(a_dictionary, key, value):
    """replaces or adds key/value in a dictionary"""
    a_dictionary[key] = value
    new_dict = {}
    for k, v in a_dictionary.items():
        new_dict[k] = v

    return new_dict
