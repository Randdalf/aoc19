#!/usr/bin/env python

"""Advent of Code 2019, Day 2 (Unit Tests)"""

import unittest

from intcode import intcode

example1 = [1, 0, 0, 0, 99]
example2 = [2, 3, 0, 3, 99]
example3 = [2, 4, 4, 5, 99, 0]
example4 = [1, 1, 1, 4, 99, 5, 6, 0, 99]
example5 = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]


class IntpointTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(
            intcode(example1).memory,
            [2, 0, 0, 0, 99]
        )

    def test_example2(slf):
        slf.assertEqual(
            intcode(example2).memory,
            [2, 3, 0, 6, 99]
        )

    def test_example3(slf):
        slf.assertEqual(
            intcode(example3).memory,
            [2, 4, 4, 5, 99, 9801]
        )

    def test_example4(slf):
        slf.assertEqual(
            intcode(example4).memory,
            [30, 1, 1, 4, 2, 5, 6, 0, 99]
        )

    def test_example5(slf):
        slf.assertEqual(
            intcode(example5).memory,
            [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
        )


if __name__ == "__main__":
    unittest.main()
