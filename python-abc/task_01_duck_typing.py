#!/usr/bin/env python3
"""
This module defines an abstract base class `Shape`
and two subclasses `Circle` and `Rectangle`.
"""

import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Abstract base class representing a shape.
    This class defines the interface for all shapes
    by declaring abstract methods.
    """

    @abstractmethod
    def area(self):
        """
        Abstract method to calculate the area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Abstract method to calculate the perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    A class representing a circle, inheriting from
    the Shape abstract base class.
    """
    def __init__(self, radius):
        """
        Initialize the Circle with a given radius.

        Args:
            radius (float): The radius of the circle.
        """
        self.radius = abs(radius)

    def area(self):
        """
        Calculate the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """
        Calculate the perimeter of the circle.

        Returns:
            float: The perimeter of the circle.
        """
        return math.pi * (self.radius * 2)


class Rectangle(Shape):
    """
    A class representing a rectangle, inheriting
    from the Shape abstract base class
    """
    def __init__(self, width, height):
        """
        Initialize the Rectangle with given width and height.

        Returns:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        return (self.width + self.height) * 2


def shape_info(shape):
    """
    Function to print the area and perimeter of a given shape.

    Args:
        shape (Shape): An object that adheres to the Shape interface.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))


# Testing the implementation
if __name__ == "__main__":
    circle = Circle(radius=6)
    rectangle = Rectangle(width=5, height=8)
    shape_info(circle)
    shape_info(rectangle)
