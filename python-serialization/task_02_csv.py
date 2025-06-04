#!/usr/bin/env python3
"""
This module provides functionality to convert data from a CSV file to a JSON file.
"""


import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert data from a CSV file to a JSON file.

    Parameters:
        csv_filename (str): The name of the CSV file to read data from.

    Returns:
        bool: True if the conversion was successful, False otherwise.
    """
    try:
        with open(csv_filename, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = []
            for row in csv_reader:
                data.append(row)
    except FileNotFoundError:
        return False

    with open('data.json', mode='w') as json_file:
        json.dump(data, json_file, indent=4)

    return True
