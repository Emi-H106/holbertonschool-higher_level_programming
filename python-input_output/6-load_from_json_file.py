#!/usr/bin/python3

import json


def load_from_json_file(filename):
    """
    A function to load an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to read from.

    Returns:
        object: The Python object converted from the JSON data.
    """
    with open(filename, 'r') as f:
        return json.load(f)
