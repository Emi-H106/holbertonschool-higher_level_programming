import unittest

from 6-max_integer import max_integer


class TestMaxInteger(unittest.TestCase):

    def test_regular_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_duplicate_values(self):
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)

    def test_single_element(self):
        self.assertEqual(max_integer([7]), 7)


if __name__ == '__main__':
    unittest.main()
