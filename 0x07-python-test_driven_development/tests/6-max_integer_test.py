#!/usr/bin/python3
"""Unittest for max_integer(list=[])"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestStringMethods(unittest.TestCase):
    
    def test_empty_list(self):
        """Test an empty list."""
        empty_list = []
        self.assertEqual(max_integer(empty_list), None)

    def test_string_list(self):
        """Test list of strings"""
        list_of_strings = ['b', 'e', 't', 't', 'y']
        self.assertEqual(max_integer(list_of_strings), 'y')

    def test_regular_list(self):
        """Test a regular list of int's"""
        regular_list = [1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(regular_list, 8)

    def test_not_int(self):
        """Test list with some elements of non-int's"""
        some_non_ints = ["a", "b", 9]
        self.assertRaises(TypeError, max_integer, some_non_ints)

    def test_negative(self):
        """Test with a list of negative int's"""
        negative_list = [-2, -6, -1]
        self.assertEqual(negative_list, -1)

    def test_float(self):
        """Test with a list with a float"""
        list_with_float = [6, 8.5, 7]
        self.assertEqual(list_with_float, 8.5)

    def test_not_list(self):
        """Test for parameter that's not a list"""
        self.assertRaises(TypeError, max_integer, 8)

    def test_one_int(self):
        """Test list with one int"""
        one_int = [8]
        self.assertEqual(one_int, 8)

    def test_identical_list(self):
        """Test a list of identical int's"""
        identical_ints = [8, 8, 8, 8, 8]
        self.assertEqual(identical_ints, 8)

    def test_strings(self):
        """Test a list of strings, instead of int's"""
        list_all_strings = ["betty", "holberton"]
        self.assertEqual(list_all_strings, "hi")

    def test_none(self):
        """Test with None as parameter"""
        self.assertRaises(TypeError, max_integer, None)

if __name__ == '__main__':
    unittest.main()
