#!/usr/bin/env python

"""Advent of Code 2019, Day 21"""

from aoc19 import solve
from intcode import IntcodeCPU


def parse(data):
    return list(map(int, data.split(',')))


spingscript = """NOT A J
NOT B T
OR T J
NOT C T
OR T J
AND D J
WALK
"""


def hull_damage(program):
    cpu = IntcodeCPU(program, *list(map(ord, spingscript)))
    cpu.execute()
    return cpu.outputs[-1]


if __name__ == "__main__":
    solve(21, parse, hull_damage)
