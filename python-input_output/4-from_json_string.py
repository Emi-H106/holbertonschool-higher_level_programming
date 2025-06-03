#!/usr/bin/python3
"""
This module provides a function to convert a JSON-formatted string
into its corresponding Python object using the standard json library.
"""


import json


def from_json_string(my_str):
    """
    Return the Python object represented by a JSON string.
    """
    return json.loads(my_str)
