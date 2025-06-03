#!/usr/bin/python3
"""
This module provides a function to append text to a file.
"""


def append_write(filename="", text=""):
    """
    Appends a specified text to the end of a UTF-8 encoded text file
    and returns the number of characters added.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
