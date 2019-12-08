#!/usr/bin/env python

"""Advent of Code 2019, Day 8 (Unit Tests)"""

import unittest

from d08 import parse
from d08 import fewest_zero_digits

example1 = parse("123456789012")


class FewestZeroDigitsTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(fewest_zero_digits(example1, 3, 2), 1)


if __name__ == "__main__":
    unittest.main()
