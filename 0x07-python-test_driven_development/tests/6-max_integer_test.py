#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_simple_complete_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([5, 2, 0, -1]), 5)
        self.assertEqual(max_integer([5, 5, 5]), 5)

    def test_simple_empty_none_list(self):
        self.assertEqual(max_integer([]), None)
        self.assertRaises(TypeError, max_integer, None)

    def test_string_comparison(self):
        self.assertRaises(TypeError, max_integer, [1, 2, 3, "Hol"])
        self.assertRaises(TypeError, max_integer, ["H", 1, 2, 3])

    def test_integer_comparison_none(self):
        self.assertRaises(TypeError, max_integer, [1, None, 2])


if __name__ == '__main__':
    unittest.main()
