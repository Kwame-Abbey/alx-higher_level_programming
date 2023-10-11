#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    """computes the square value of all integers of a matrix"""
    new_list = []
    for row in range(len(matrix)):
        new_list.append(list(map(lambda x: x * x, matrix[row])))

    return new_list
