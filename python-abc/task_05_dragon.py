#!/usr/bin/env python3
"""
This module showing examples of mixins
"""


class SwimMixin:
    """
    A mixin class for swim
    """
    def swim(self):
        """
        Print a message
        """
        print("The creature swims!")


class FlyMixin:
    """
    A mixin class for fly
    """
    def fly(self):
        """
        Print a message
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    A class representing a Dragon that inherits the SwimMixin and the FlyMixin classes
    """
    def roar(self):
        """
        Print a message
        """
        print("The dragon roars!")


# Testing the implementation
if __name__ == "__main__":
    draco = Dragon()
    draco.swim()
    draco.fly()
    draco.roar()
