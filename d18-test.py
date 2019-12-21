#!/usr/bin/env python

"""Advent of Code 2019, Day 18 (Unit Tests)"""

import unittest

from d18 import parse, shortest_path, quad_droid

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

example6 = parse("""#######
#a.#Cd#
##...##
##.@.##
##...##
#cB#Ab#
#######""")

example7 = parse("""###############
#d.ABC.#.....a#
######...######
######.@.######
######...######
#b.....#.....c#
###############""")

example8 = parse("""#############
#DcBa.#.GhKl#
#.###...#I###
#e#d#.@.#j#k#
###C#...###J#
#fEbA.#.FgHi#
#############""")

example9 = parse("""#############
#g#f.D#..h#l#
#F###e#E###.#
#dCba...BcIJ#
#####.@.#####
#nK.L...G...#
#M###N#H###.#
#o#m..#i#jk.#
#############""")


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


class QuadDroidTests(unittest.TestCase):
    def test_example6(slf):
        return slf.assertEqual(quad_droid(example6), 8)

    def test_example7(slf):
        return slf.assertEqual(quad_droid(example7), 24)

    def test_example8(slf):
        return slf.assertEqual(quad_droid(example8), 32)

    def test_example9(slf):
        return slf.assertEqual(quad_droid(example9), 72)


if __name__ == "__main__":
    unittest.main()
