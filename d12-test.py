#!/usr/bin/env python

"""Advent of Code 2019, Day 12 (Unit Tests)"""

import unittest

from d12 import parse
from d12 import total_energy
from d12 import steps_until_repeat

example1 = """<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>"""

example2 = """<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>"""


class TotalEnergyTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(total_energy(parse(example1), 10), 179)

    def test_example2(slf):
        slf.assertEqual(total_energy(parse(example2), 100), 1940)


class StepsUntilRepeatTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(steps_until_repeat(parse(example1)), 2772)

    def test_example2(slf):
        slf.assertEqual(steps_until_repeat(parse(example2)), 4686774924)


if __name__ == "__main__":
    unittest.main()
