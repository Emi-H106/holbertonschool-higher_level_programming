#!/usr/bin/env python3
"""
This module defines two parent class "Fish" and "Bird".
"""


class Fish:
    """
    A class representing a Fish
    """
    def swim(self):
        """
        Print a message 

        """
        print("The fish is swimming")

    def habitat(self):
        """
        Print a message
        """
        print("The fish lives in water")


class Bird:
    """
    A class representing a Bird
    """
    def fly(self):
        """
        Print a message
        """
        print("The bird is flying")

    def habitat(self):
        """
        Print a message
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    A class representing a Flying fish that inherits the Fish and the Bird classes
    """
    def fly(self):
        """
        Print a message
        """
        print("The flying fish is soaring!")

    def swim(self):
        """
        Print a message
        """
        print("The flying fish is swimming!")

    def habitat(self):
        """
        Print a message
        """
        print("The flying fish lives both in water and the sky!")


# Testing
if __name__ == "__main__":
    flying_fish = FlyingFish()
    flying_fish.fly()
    flying_fish.swim()
    flying_fish.habitat()
    print(FlyingFish.mro())
