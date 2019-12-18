#!/usr/bin/env python

"""Advent of Code 2019, Day 18 (Unit Tests)"""

import unittest

from d18 import parse, shortest_path

example1 = parse("""#########
#b.A.@.a#
#########""")

example2 = parse("""########################
#f.D.E.e.C.b.A.@.a.B.c.#
######################.#
#d.....................#
########################""")

example3 = parse("""########################
#...............b.C.D.f#
#.######################
#.....@.a.B.c.d.A.e.F.g#
########################""")

example4 = parse("""#################
#i.G..c...e..H.p#
########.########
#j.A..b...f..D.o#
########@########
#k.E..a...g..B.n#
########.########
#l.F..d...h..C.m#
#################""")

example5 = parse("""########################
#@..............ac.GI.b#
###d#e#f################
###A#B#C################
###g#h#i################
########################""")


class ShortestPathTests(unittest.TestCase):
    def test_example1(slf):
        return slf.assertEqual(shortest_path(example1), 8)

    def test_example2(slf):
        return slf.assertEqual(shortest_path(example2), 86)

    def test_example3(slf):
        return slf.assertEqual(shortest_path(example3), 132)

    def test_example4(slf):
        return slf.assertEqual(shortest_path(example4), 136)

    def test_example5(slf):
        return slf.assertEqual(shortest_path(example5), 81)


if __name__ == "__main__":
    unittest.main()
