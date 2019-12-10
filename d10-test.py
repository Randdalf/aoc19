#!/usr/bin/env python

"""Advent of Code 2019, Day 10 (Unit Tests)"""

import unittest

from d10 import parse
from d10 import best_location
from d10 import vaporized_200

example1 = parse("""......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####""")

example2 = parse("""#.#...#.#.
.###....#.
.#....#...
##.#.#.#.#
....#.#.#.
.##..###.#
..#...##..
..##....##
......#...
.####.###.""")

example3 = parse(""".#..#..###
####.###.#
....###.#.
..###.##.#
##.##.#.#.
....###..#
..#.#..#.#
#..#.#.###
.##...##.#
.....#.#..""")

example4 = parse(""".#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##""")


class BestLocationTests(unittest.TestCase):
    def test_example1(slf):
        return slf.assertEqual(best_location(example1), 33)

    def test_example2(slf):
        return slf.assertEqual(best_location(example2), 35)

    def test_example3(slf):
        return slf.assertEqual(best_location(example3), 41)

    def test_example4(slf):
        return slf.assertEqual(best_location(example4), 210)


class Vaporized200Tests(unittest.TestCase):
    def test_example4(slf):
        return slf.assertEqual(vaporized_200(example4), 802)


if __name__ == "__main__":
    unittest.main()
