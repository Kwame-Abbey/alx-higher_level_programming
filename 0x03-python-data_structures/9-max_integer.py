#!/usr/bin/python3


def max_integer(my_list=[]):
    """finds the biggest integer of a list"""
    if len(my_list) == 0:
        return None
    int_max = my_list[0]
    for num in my_list:
        if num > int_max:
            int_max = num
    return int_max
