#!/usr/bin/env python

"""Advent of Code 2019, Day 2 (Unit Tests)"""

import unittest

from d02 import intpoint


class IntpointTests(unittest.TestCase):
    def test_example1(slf):
        program = [1, 0, 0, 0, 99]
        slf.assertEqual(intpoint(program), 2)
        slf.assertEqual(program, [2, 0, 0, 0, 99])

    def test_example2(slf):
        program = [2, 3, 0, 3, 99]
        slf.assertEqual(intpoint(program), 2)
        slf.assertEqual(program, [2, 3, 0, 6, 99])

    def test_example3(slf):
        program = [2, 4, 4, 5, 99, 0]
        slf.assertEqual(intpoint(program), 2)
        slf.assertEqual(program, [2, 4, 4, 5, 99, 9801])

    def test_example4(slf):
        program = [1, 1, 1, 4, 99, 5, 6, 0, 99]
        slf.assertEqual(intpoint(program), 30)
        slf.assertEqual(program, [30, 1, 1, 4, 2, 5, 6, 0, 99])

    def test_example5(slf):
        program = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
        slf.assertEqual(intpoint(program), 3500)
        slf.assertEqual(
            program,
            [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
        )


if __name__ == "__main__":
    unittest.main()
