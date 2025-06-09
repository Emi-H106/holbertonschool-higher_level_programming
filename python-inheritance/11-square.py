#!/usr/bin/python3
"""
Module for a base class for geometry-related operations.
"""


class BaseGeometry:
    """
    A base class for geometry-related operations.
    """
    def area(self):
        """
        Calculate the area of the geometry.

        Raises:
            Exception: Indicates that the area method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate that the value is a positive integer.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to validate.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle, inheriting from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """

        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            A string representation of the rectangle.
        """

        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """
     A class that representing a Square,inheriting from Rectangle.
    """

    def __init__(self, size):
        """
        Initialize a new Square.

        Args:
            size(int): The size of the new square.
        """

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Calculate the area of the square

        Returns:
            int: The area of the square
        """

        return self.__size ** 2

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            A string representation of the square.
        """

        return "[Square] {}/{}".format(self.__size, self.__size)
