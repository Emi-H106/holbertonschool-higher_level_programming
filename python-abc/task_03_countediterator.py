#!/usr/bin/env python3
"""
This module provides a custom iterator class, CountedIterator
"""


class CountedIterator:
    """
    A custom iterator that counts the number of items iterated over.
    """
    def __init__(self, some_iterable):
        """
        Initialize the CountedIterator with an iterable.

        Args:
            iterable: An iterable object (e.g., list, tuple)
            to be iterated over.
        """
        self.iterator = iter(some_iterable)
        self.count = 0

    def get_count(self):
        """
        Get the current count of items that have been iterated over.

        returns:
            int: The number of items fetched so far.
        """
        return self.count

    def __next__(self):
        """
        Fetch the next item from the iterator and increment the count.

        returns:
            The next item in the iterator.

        Raises:
            StopIteration: If there are no more items to iterate over.
        """
        item = next(self.iterator)
        self.count += 1
        return item


# Testing the implementation
if __name__ == "__main__":
    data = [5, 6, 7, 8]
    counted_iter = CountedIterator(data)

    try:
        while True:
            item = next(counted_iter)
            print(
                f"Got {item}, total {counted_iter.get_count()} items iterated."
                 )
    except StopIteration:
        print("No more items.")
