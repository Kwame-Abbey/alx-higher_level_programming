#!/usr/bin/python3
def safe_print_integer(value):
    """ prints an integer with "{:d}".format()"""
    is_integer = True
    try:
        print("{:d}".format(value))
    except ValueError:
        is_integer = False
    if is_integer:
        return True
    else:
        return False
