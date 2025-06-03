#!/usr/bin/python3
"""
This script adds command line arguments to a list and saves it to
'add_item.json' in JSON format, creating the file if it does not exist.
"""

import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_items_to_list_and_save():
    """
    A function to add command line arguments to a list
    and save them to a JSON file.
    """
    try:
        existing_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        existing_list = []

    new_items = sys.argv[1:]
    existing_list.extend(new_items)

    save_to_json_file(existing_list, "add_item.json")


if __name__ == "__main__":
    add_items_to_list_and_save()
