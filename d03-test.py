#!/usr/bin/env python

"""Advent of Code 2019, Day 3 (Unit Tests)"""

import unittest

from d03 import parse
from d03 import closest_intersection
from d03 import fewest_steps_intersection


example1 = parse("""R8,U5,L5,D3
U7,R6,D4,L4""")

example2 = parse("""R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83""")

example3 = parse("""R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7""")


class ClosestIntersectionTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(closest_intersection(example1), 6)

    def test_example2(slf):
        slf.assertEqual(closest_intersection(example2), 159)

    def test_example3(slf):
        slf.assertEqual(closest_intersection(example3), 135)


class FewestStepsIntersetion(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(fewest_steps_intersection(example1), 30)

    def test_example2(slf):
        slf.assertEqual(fewest_steps_intersection(example2), 610)

    def test_example3(slf):
        slf.assertEqual(fewest_steps_intersection(example3), 410)


if __name__ == "__main__":
    unittest.main()
