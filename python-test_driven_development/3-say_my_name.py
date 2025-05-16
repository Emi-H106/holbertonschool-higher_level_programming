#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    """
    Prints a message in the format "My name is <first_name> <last_name>".

    Parameters:
    first_name(str):The first name. Must be string.
    last_name(str): The last name. Must be string.

    Raise:
    TypeError: If either 'first_name' or 'last_name' is not a string.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {0} {1}".format(first_name, last_name).strip())
