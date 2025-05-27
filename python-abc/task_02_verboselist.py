#!/usr/bin/env python3
"""
This module provides a custom list class named VerboseList
that extends the built-in list class.
VerboseList prints notification messages whenever
items are added or removed from the list.
"""


class VerboseList(list):
    """
    A custom list class that extends the built-in list class.
    """
    def append(self, item):
        """
        Append an item to the end of the list and print a notification message.

        Args:
            item: The item to be added to the list.
        """
        super().append(item)
        print("Added [{}]  to the list.".format(item))

    def extend(self, items):
        """
        Extend the list by appending all the items from
        the iterable and print a notification message.

        Args:
            items: The items to be added to the list.
        """
        super().extend(items)
        print("Extended the list with [{}]  items.".format(len(items)))

    def remove(self, item):
        """
        Remove the first occurrence of an item from the list
        and print a notification message.

        Args:
            item: The item to be removed from the list.
        """
        print("Removed [{}]  from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """
         Remove the item at the given position in the list, and return it.
         Print a notification message before removing the item.

        Args:
            index (int, optional): The index of the item to be removed.
            Defaults to -1.

        Retuens:
            The item that was removed from the list.
        """
        item = self[index]
        print("Popped [{}]  from the list.".format(item))
        return super().pop(index)


# Test the VerboseList class
if __name__ == "__main__":
    vl = VerboseList([4, 5, 6])
    vl.append(7)
    vl.extend([8, 9])
    vl.remove(4)
    vl.pop()
    vl.pop(0)
