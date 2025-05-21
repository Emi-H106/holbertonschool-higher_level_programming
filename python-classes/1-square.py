#!/usr/bin/python3
"""
This module defines a simple Square class
"""


class Square:
    """Class Square that defines a square by size."""
    def __init__(self, size):
        """
        Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size
