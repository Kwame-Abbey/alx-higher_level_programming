#!/usr/bin/python3


def best_score(a_dictionary):
    """returns a key with the biggest integer value"""
    if a_dictionary:
        highest_value = 0
        for key, value in a_dictionary.items():
            if value > highest_value:
                highest_value = value
        for k, v in a_dictionary.items():
            if v == highest_value:
                highest_value_key = k
        return highest_value_key
    else:
        return None
