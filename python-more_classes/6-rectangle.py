#!/usr/bin/python3
"""
Module for defining a Rectangle class.
"""


class Rectangle:
    """
    A class used to represent a Rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        number_of_instances (int): The number of Rectangle instances.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.Defaults to 0.
            height (int): The height of the new rectangle.DEfaults to 0.
        """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Retrieve the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): The width of rectangle.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        Retrieve the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): The height of rectangle.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """

        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            result = 0
        else:
            result = 2 * (self.__width + self.__height)

        return result

    def __str__(self):
        """
        Returns a string representation of the rectangle using '#' characters.

        Returns:
            str: The string representation of the rectangle.
        """

        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle_str = ""
        for _ in range(self.__height):
            rectangle_str += "#" * self.__width + "\n"

        return rectangle_str.rstrip("\n")

    def __repr__(self):
        """
        Returns a string representation of the rectangle
        to recreate a new instance using eval().

        Returns:
            str: The string representation of the rectangle.
        """

        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Prints a message when an instance of Rectangle is deleted.
        """

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
