#!/usr/bin/python3
import sys
if __name__ == "__main__":
    number_of_arguments = len(sys.argv)
    sum_of_arguments = 0
    for arg in range(1, number_of_arguments):
        sum_of_arguments += int(sys.argv[arg])
    print(sum_of_arguments)
