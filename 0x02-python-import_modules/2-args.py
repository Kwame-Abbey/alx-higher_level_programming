#!/usr/bin/python3
import sys
if __name__ == "__main__":
    number_of_arguments = len(sys.argv) - 1
    if number_of_arguments == 0:
        print(f"{number_of_arguments} arguments.")
    elif number_of_arguments == 1:
        print(f"{number_of_arguments} argument:")
        for arg in range(1, number_of_arguments + 1):
            print(f"{arg}: {sys.argv[arg]}")
    else:
        print(f"{number_of_arguments} arguments:")
        for arg in range(1, number_of_arguments + 1):
            print(f"{arg}: {sys.argv[arg]}")
