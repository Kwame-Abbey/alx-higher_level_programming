#!/usr/bin/python3
"""Defines serialization of a class"""


def class_to_json(obj):
    """serializes an object of a class"""
    return obj.__dict__
