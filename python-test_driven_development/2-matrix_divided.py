#!/usr/bin/python3

"""
This module provides a function to divide all elements
of a matrix by a given number.
Each element is divided and rounded to 2 decimal places.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix (list of list of int/float): The matrix to divide.
        div (int/float): The divisor.


    Returns:
        list of list of float: A new matrix with each value divided by div.


    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                    or if rows of matrix are not the same size,
                    or if div is not a number.
        ZeroDivisionError: If div is zero.
    """

    if not isinstance(matrix, list) or not all(
        isinstance(row, list) for row in matrix
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(x, (int, float)) for row in matrix for x in row):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    row_lengths = [len(row) for row in matrix]
    if not all(length == row_lengths[0] for length in row_lengths):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(x / div, 2) for x in row] for row in matrix]

    return new_matrix
