#!/usr/bin/env python3

from abc import ABC, abstractmethod

class Animal(ABC):
    """
    Abstract base class representing an Animal.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method to be implemented by subclasses.
        """
        pass


class Dog(Animal):
    """
    A class representing a Dog, which is a subclass of Animal.
    """

    def sound(self):
        """
        Returns the sound that a dog makes.

        Returns:
            str: The string "Bark".
        """
        return "Bark"


class Cat(Animal):
    """
    A class representing a Cat, which is a subclass of Animal.
    """

    def sound(self):
        """
        Returns the sound that a cat makes.

        Returns:
            str: The string "Meow".
        """
        return "Meow"
