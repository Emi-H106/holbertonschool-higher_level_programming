#!/usr/bin/env python3
"""
Module for serializing a Python dictionary to XML and
deserializing it back to a dictionary.
"""


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary into an XML file.

    Parameters:
        dictionary (dict): The dictionary to be serialized.
        filename (str): The name of the file where the XML data will be saved.
    """
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)

def deserialize_from_xml(filename):
    """
    Deserialize an XML file back into a Python dictionary.

    Parameters:
        filename (str): The name of the XML file to be deserialized.

    Returns:
        dict: The deserialized dictionary.
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    dictionary = {}

    for child in root:
        dictionary[child.tag] = child.text

    return dictionary
