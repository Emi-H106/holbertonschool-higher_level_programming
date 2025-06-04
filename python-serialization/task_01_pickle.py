#!/usr/bin/env python3
"""
This module allows for serializing and deserializing custom
Python objects using the pickle module.
"""


import pickle


class CustomObject:
    """
    A custom class representing an object with attributes
    name, age, and is_student.
    """

    def __init__(self, name, age, is_student):
        """
        Initialize a CustomObject with a name, age, and student status.

        Parameters:
            name (str): The name of the person.
            age (int): The age of the person.
            is_student (boolean): The student status of the person.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the attributes of the CustomObject.
        """
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """
        Serialize the current instance of CustomObject and
        save it to the provided filename.

        Parameters:
             filename (str): The name of the file to save
             the serialized object.

        Returns:
            None
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print("Error during serialization: {}".format(e))
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Load and return an instance of CustomObject from
        the provided filename.

        Parameters:
            filename (str): The name of the file to load
                            the serialized object from.

        Returns:
            CustomObject: An instance of CustomObject loaded
                          from the file, or None if an error occurs.
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except Exception as e:
            print("Error during deserialization: {}".format(e))
            return None
