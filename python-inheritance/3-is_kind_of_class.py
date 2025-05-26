#!/usr/bin/python3
"""
A module that checks if an object is an instance of a specified class,
or if the object is an instance of a class that inherits from
a specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of, or if the object is
    an instance of a class that inherited from, the specified class.
    """
    return isinstance(obj, a_class)
