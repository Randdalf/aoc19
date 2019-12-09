#!/usr/bin/env python

"""Advent of Code 2019, Day 9"""

from aoc19 import solve

from intcode import intcode


def parse(data):
    return list(map(int, data.split(',')))


def boost_keycode(program):
    return intcode(program, 1).outputs[0]


def distress_coords(program):
    return intcode(program, 2).outputs[0]


if __name__ == "__main__":
    solve(9, parse, boost_keycode, distress_coords)
