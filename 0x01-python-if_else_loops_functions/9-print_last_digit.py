#!/usr/bin/python3


def print_last_digit(n):
    last_digit_unsigned = abs(n) % 10
    print(last_digit_unsigned, end="")
    return last_digit_unsigned
