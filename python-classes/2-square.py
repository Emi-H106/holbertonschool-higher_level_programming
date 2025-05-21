#!/usr/bin/python3
"""
This module defines a simple Square class
"""


class Square:
    """Class Square that defines a square by size."""
    def __init__(self, size=0):
        """
        Initialize a new Square.

        Args:
            size (int): The size of the new square.

        Raises:
            TypeError: If size is not an integer.
            alueError: If size is less than 0.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
