#!/usr/bin/env python

"""Advent of Code 2019, Day 22 (Unit Tests)"""

import unittest

from d22 import parse, shuffle

example1 = """deal with increment 7
deal into new stack
deal into new stack"""

example2 = """cut 6
deal with increment 7
deal into new stack"""

example3 = """deal with increment 7
deal with increment 9
cut -2"""

example4 = """deal into new stack
cut -2
deal with increment 7
cut 8
cut -4
deal with increment 7
cut 3
deal with increment 9
deal with increment 3
cut -1"""


class ShuffleTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(
            shuffle(parse(example1), 10),
            [0, 3, 6, 9, 2, 5, 8, 1, 4, 7]
        )

    def test_example2(slf):
        slf.assertEqual(
            shuffle(parse(example2), 10),
            [3, 0, 7, 4, 1, 8, 5, 2, 9, 6]
        )

    def test_example3(slf):
        slf.assertEqual(
            shuffle(parse(example3), 10),
            [6, 3, 0, 7, 4, 1, 8, 5, 2, 9]
        )

    def test_example4(slf):
        slf.assertEqual(
            shuffle(parse(example4), 10),
            [9, 2, 5, 8, 1, 4, 7, 0, 3, 6]
        )

if __name__ == "__main__":
    unittest.main()
