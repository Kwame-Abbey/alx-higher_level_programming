#!/usr/bin/python3


def fizzbuzz():
    """prints numbers from 1 to 100"""
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print(f"{'FizzBuzz'}", end=" ")
        elif num % 3 == 0:
            print(f"{'Fizz'}", end=" ")
        elif num % 5 == 0:
            print(f"{'Buzz'}", end=" ")
        else:
            print(num, end=" ")
