#!/usr/bin/python3
"""
This module provides a custom list class, `MyList`,
which inherits from Python's built-in `list` class.
"""


class MyList(list):
    """
    A custom list class that inherits from the built-in list class.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        """
        print(sorted(self))

    def __str__(self):
        """
        Returns a string representation of the list.
        """
        return str(self)
