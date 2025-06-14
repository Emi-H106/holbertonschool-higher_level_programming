#!/usr/bin/python3
"""
This module defines the Student class for storing a student’s name
and age, and provides a method to get their information
as a dictionary.
"""


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

    def to_json(self):
        """
        Retrieve a dictionary representation of the Student instance.

        Returns:
            dict: A dictionary containing the student's first name,
                  last name, and age.
        """
        return {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
                }
