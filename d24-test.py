#!/usr/bin/env python

"""Advent of Code 2019, Day 24 (Unit Tests)"""

import unittest

from d24 import parse, biodiversity_rating

example1 = """....#
#..#.
#..##
..#..
#...."""


class BiodiversityRatingTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(biodiversity_rating(parse(example1)), 2129920)


if __name__ == "__main__":
    unittest.main()
