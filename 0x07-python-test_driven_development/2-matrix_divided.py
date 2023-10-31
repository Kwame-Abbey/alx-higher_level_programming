#!/usr/bin/python3
"""Divides each element of a matrix by a specific divisor"""


def matrix_divided(matrix, div):
    """
    Computes the quotient of the element of a matrix rounded
    to two (2) decimal places

    Args:
        matrix: A 2d matrix
        div: Divisor to divided elements by

    Returns:
        The quotient of the division rounded to 2 decimal places
    """
    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    length_of_first_row = len(matrix[0])
    new_matrix = []
    for i in range(len(matrix)):
        each_row = []
        for j in range(len(matrix[i])):
            if length_of_first_row != len(matrix[i]):
                raise TypeError('Each row of the matrix must'
                                ' have the same size')
            if type(matrix[i][j]) is not int\
                    and type(matrix[i][j]) is not float:
                raise TypeError('matrix must be a matrix'
                                ' (list of lists) of integers/floats')

            each_element = round(matrix[i][j] / div, 2)
            each_row.append(each_element)
        new_matrix.append(each_row)

    return new_matrix
