#!/usr/bin/python3


def print_last_digit(n):
    """Prints last digit of a numberr"""
    last_digit_unsigned = abs(n) % 10
    print(last_digit_unsigned, end="")
    return last_digit_unsigned
