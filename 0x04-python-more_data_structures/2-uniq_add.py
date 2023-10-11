#!/usr/bin/python3


def uniq_add(my_list=[]):
    """adds all unique integers in a list (only once for each integer)"""
    my_set = set()
    result = 0
    for element in my_list:
        my_set.add(element)

    for element in my_set:
        result += element

    return result
