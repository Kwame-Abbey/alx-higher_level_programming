#!/usr/bin/python3


def remove_char_at(str, n):
    """copies a string and removes character at given index"""
    copied_str = ""
    for idx in range(len(str)):
        if idx != n:
            copied_str = copied_str + str[idx]
    return copied_str
