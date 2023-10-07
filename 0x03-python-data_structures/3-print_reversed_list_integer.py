#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    """Prints all integers of a list in reverse order"""
    if my_list:
        list_length = len(my_list)
        for i in range(list_length - 1, -1, -1):
            print("{:d}".format(my_list[i]))
    else:
        pass
