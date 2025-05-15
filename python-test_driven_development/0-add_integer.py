#!/usr/bin/python3

"""
This module provides a function to add two integers.
"""

def add_integer(a, b=98):
    """
    Adds two numbers.

    Args:
        a (integers or floats): The first number.
        b (integers or floats): The second number. Default to 98.

    Returns:
        int: The addition of a and b.

    Raises:
        TypeError:If a and b not intergers or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
