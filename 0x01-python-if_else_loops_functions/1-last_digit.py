#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)


def last_d(n):
    last_unsigned = abs(n) % 10
    if n < 0:
        return -last_unsigned
    else:
        return last_unsigned


last_digit = last_d(number)
if last_digit > 5:
    print(f"Last digit of {number:d} is {last_digit:d} and is greater than 5")
elif last_digit == 0:
    print(f"Last digit of {number:d} is {last_digit:d} and is 0")
elif last_digit < 6:
    print(f"Last digit of {number:d} is {last_digit:d} and is less than 6"
          " and not 0")
