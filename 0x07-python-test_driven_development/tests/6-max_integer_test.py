#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        actual = max_integer([1, 2, 3, 4])
        expected = 4
        self.assertEqual(actual, expected)
        actual = max_integer()
        expected = None
        self.assertEqual(actual, expected)

    def test_max_integer_error(self):
        with self.assertRaises(TypeError):
            max_integer(8)

    def test_same(self):
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)
        self.assertEqual(max_integer([-1, -1, -1, -1]), -1)

    def test_type(self):
        self.assertIs(list, list)

    def test_twoMax(self):
        self.assertEqual(max_integer([2, 2, 0, -1]), 2)
        self.assertEqual(max_integer([-1, 0, 0, -1]), 0)

    def test_oneArg(self):
        self.assertEqual(max_integer([1]), 1)

    def test_floats(self):
        self.assertEqual(max_integer([0.0, 0, 1]), 1)
        self.assertEqual(max_integer([1.0, 0, 0.0]), 1)

    def test_invalid(self):
        self.assertRaises(TypeError, max_integer, [1, "cat", 3],
                          msg="unorderable types: str() > int()")
        self.assertRaises(TypeError, max_integer, [1, 0, "7"],
                          msg="unorderable types: str() > int()")

    def test_weird(self):
        self.assertEqual(max_integer([1, 0, 00]), 1)
