#!/usr/bin/python3
"""
Module for generating Pascal's triangle.
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.

    Parameters:
         n (int): The number of rows to generate.

    Returns:
        list of lists of int: Pascal's triangle represented as a list of lists.
    """
    triangle = []

    if n <= 0:
        return triangle

    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)

    return triangle
