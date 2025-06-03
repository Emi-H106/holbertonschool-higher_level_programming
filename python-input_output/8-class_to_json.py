#!/usr/bin/python3
"""
This module provides a function to convert a Python object to
a dictionary suitable for JSON serialization.
"""


def class_to_json(obj):
    """
    Return the dictionary description with simple data
    structure for JSON serialization of an object.
    """
    return vars(obj)
