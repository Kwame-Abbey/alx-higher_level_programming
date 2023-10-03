#!/usr/bin/python3


def uppercase(str):
    """Prints a string in uppercase"""
    result = ""
    for i in str:
        if 97 <= ord(i) <= 122:
            new_value = ord(i) - 32
            result += chr(new_value)
        else:
            result += i

    print("{}".format(result))
