#!/usr/bin/env python

"""Advent of Code 2019, Day 6 (Unit Tests)"""

import unittest

from d06 import parse, orbit_count_checksum


example1 = parse("""COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L""")


class OrbitCountChecksum(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(orbit_count_checksum(example1), 42)


if __name__ == "__main__":
    unittest.main()
