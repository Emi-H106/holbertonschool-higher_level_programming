#!/usr/bin/python3

import json


def save_to_json_file(my_obj, filename):
    """
    A function to save an object to a file in JSON format.

    Args:
        my_obj: An object that can be serialized to JSON.
        filename (str): The name of the file to save to.
    """
    with open(filename, 'w') as f:
        return json.dump(my_obj, f)
