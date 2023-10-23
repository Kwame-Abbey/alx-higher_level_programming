#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """prints the first x elements of a list and only integers"""
    length = 0
    should_continue = False
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
            length += 1
        except (ValueError, TypeError):
            should_continue = True
        if should_continue:
            continue
    print()
    return length
