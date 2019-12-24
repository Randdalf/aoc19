#!/usr/bin/env python

"""Advent of Code 2019, Day 24 (Unit Tests)"""

import unittest

from d24 import parse, biodiversity_rating, recursive_bugs

example1 = """....#
#..#.
#..##
..#..
#...."""


class BiodiversityRatingTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(biodiversity_rating(parse(example1)), 2129920)


class RecursiveBugsTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(recursive_bugs(parse(example1), minutes=10), 99)


if __name__ == "__main__":
    unittest.main()
