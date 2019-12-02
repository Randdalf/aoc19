#!/usr/bin/env python

"""Advent of Code 2019, Day 1 (Unit Tests)"""

import unittest

from d01 import fuel_requirement
from d01 import true_fuel_requirement


class FuelRequirementTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(fuel_requirement(12), 2)

    def test_example2(slf):
        slf.assertEqual(fuel_requirement(14), 2)

    def test_example3(slf):
        slf.assertEqual(fuel_requirement(1969), 654)

    def test_example4(slf):
        slf.assertEqual(fuel_requirement(100756), 33583)


class TrueFuelRequirementTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(true_fuel_requirement(14), 2)

    def test_example2(slf):
        slf.assertEqual(true_fuel_requirement(1969), 966)

    def test_example3(slf):
        slf.assertEqual(true_fuel_requirement(100756), 50346)


if __name__ == "__main__":
    unittest.main()
