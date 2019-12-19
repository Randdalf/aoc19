#!/usr/bin/env python

"""Advent of Code 2019, Day 19"""

from itertools import product

from aoc19 import solve
from intcode import intcode


def parse(data):
    return list(map(int, data.split(',')))


def points_in_beam(program):
    outputs = []
    for x, y in product(range(50), range(50)):
        outputs.extend(intcode(program, x, y).outputs)
    return sum(outputs)


if __name__ == "__main__":
    solve(19, parse, points_in_beam)
