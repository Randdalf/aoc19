#!/usr/bin/env python

"""Advent of Code 2019, Day 4 (Unit Tests)"""

import unittest

from d04 import is_password
from d04 import is_true_password


class IsPasswordTests(unittest.TestCase):
    def test_example1(slf):
        return slf.assertEqual(is_password(111111), True)

    def test_example2(slf):
        return slf.assertEqual(is_password(223450), False)

    def test_example3(slf):
        return slf.assertEqual(is_password(123789), False)


class IsTruePasswordTests(unittest.TestCase):
    def test_example1(slf):
        return slf.assertEqual(is_true_password(112233), True)

    def test_example2(slf):
        return slf.assertEqual(is_true_password(123444), False)

    def test_example3(slf):
        return slf.assertEqual(is_true_password(111122), True)


if __name__ == "__main__":
    unittest.main()
