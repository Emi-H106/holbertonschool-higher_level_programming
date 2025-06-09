#!/usr/bin/python3
"""
This module provides a function to convert a Python
object to its JSON string representation.
"""


import json


def to_json_string(my_obj):
    """
    Return the JSON representation of an object (string).
    """
    return json.dumps(my_obj)
