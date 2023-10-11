#!/usr/bin/python3


def search_replace(my_list, search, replace):
    """replaces all occurrences of an element by another in a new list."""
    new_list = []
    for element in my_list:
        if element == search:
            element = replace
            new_list.append(element)
        else:
            new_list.append(element)

    return new_list
