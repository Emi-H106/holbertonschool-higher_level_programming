#!/usr/bin/python3


class Student:
    """
    A class representing a student with first name,
    last name, and age attributes.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance with first name, last name, and age.

        Parameters:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
            """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of the Student instance.

        Parameters:
            attrs (list of str) : A list of attribute names to
                                  include in the dictionary.
                                  If None, all attributes are included.

        Returns:
            dict: A dictionary containing the specified attributes
            of the student.
        """
        if attrs is None:
            return {
                     'first_name': self.first_name,
                     'last_name': self.last_name,
                     'age': self.age
                    }
        else:
            result = {}
            for attr in attrs:
                if hasattr(self, attr):
                    result[attr] = getattr(self, attr)
            return result
