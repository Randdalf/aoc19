#!/usr/bin/env python

"""Advent of Code 2019, Day 6 (Unit Tests)"""

import unittest

from d06 import parse
from d06 import orbit_count_checksum
from d06 import orbital_transfers


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


example2 = parse("""COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN""")


class OrbitCountChecksumTest(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(orbit_count_checksum(example1), 42)


class OrbitalTransfersTests(unittest.TestCase):
    def test_example2(slf):
        slf.assertEqual(orbital_transfers(example2), 4)


if __name__ == "__main__":
    unittest.main()
