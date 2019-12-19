#!/usr/bin/env python

"""Advent of Code 2019, Day 19"""

from itertools import product

from aoc19 import solve
from intcode import intcode


def parse(data):
    return list(map(int, data.split(',')))


def in_beam(program, x, y):
    return intcode(program, x, y).outputs[0]


def points_in_beam(prog):
    return sum(in_beam(prog, x, y) for x, y in product(range(50), range(50)))


def santa_ship_coord(program, width=100, height=100):
    y = 10
    left = 0
    right = 10
    while True:
        right += 2
        while not in_beam(program, left, y):
            left += 1
        max_add = 0
        while not in_beam(program, right, y):
            right -= 1
        if right - left >= width - 1:
            top = y - (height - 1)
            tl = in_beam(program, left, top)
            tr = in_beam(program, left + width - 1, top)
            if tl and tr:
                return left * 10000 + top
        y += 1


if __name__ == "__main__":
    solve(19, parse, points_in_beam, santa_ship_coord)
