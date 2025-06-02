#!/usr/bin/python3

def write_file(filename="", text=""):
    """
    Writes a given string to a text file using UTF-8 encoding
    and returns the number of characters written.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
