#!/usr/bin/python3
"""
This module provides a function to inspect the attributes
and methods of an object.
"""


def lookup(obj):
    """
    Returns a list of the available attributes and methods of an object.

    Parameters:
    obj: The object to inspect. This can be an instance of
         a class, a module, a function, etc.

    Returns:
    list: A list of the names of the attributes and methods of the object.
    """

    return dir(obj)
