#!/usr/bin/python3


def common_elements(set_1, set_2):
    """ returns a set of common elements in two sets"""
    common_set = {x for x in set_1 if x in set_2}
    return common_set
