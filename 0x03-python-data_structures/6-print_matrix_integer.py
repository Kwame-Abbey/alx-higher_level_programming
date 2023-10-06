#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    """prints a matrix of integers"""
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            if column < len(matrix[0]) - 1:
                print("{:d}".format(matrix[row][column]), end=" ")
            else:
                print("{:d}".format(matrix[row][column]))
