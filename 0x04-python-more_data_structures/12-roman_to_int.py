#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    int_sum = 0
    conv = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for current, next in zip(roman_string, roman_string[1:]):
        if conv[current] >= conv[next]:
            int_sum += conv[current]
        else:
            int_sum -= conv[current]
    int_sum += conv[roman_string[-1]]
    return int_sum
