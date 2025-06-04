#!/usr/bin/env python3
"""
This module provides functionality to serialize a Python dictionary
to a JSON file and deserialize the JSON file back to
a Python dictionary.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary to a JSON file.

    Parameters:
        data (dict): A Python Dictionary with data to be serialized.
        filename (str): The name of the file where the JSON data will be saved.
    """
    with open(filename, 'w') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Loads and deserializes data from a JSON file to a
    Python dictionary.

    Parameters:
        filename (str): The name of the file from which
                        the JSON data will be loaded.

    Returns:
        dict: A Python Dictionary with the deserialized
        JSON data from the file.
    """
    with open(filename, 'r') as file:
        return json.load(file)
