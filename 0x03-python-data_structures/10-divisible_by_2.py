#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    """ finds all multiples of 2 in a list"""
    div_list = []
    for num in my_list:
        if num % 2 == 0:
            div_list.append(True)
        else:
            div_list.append(False)

    return div_list
