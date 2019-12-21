#!/usr/bin/env python

"""Advent of Code 2019, Day 21"""

from aoc19 import solve
from intcode import intcode


def parse(data):
    return list(map(int, data.split(',')))


walk = """OR A J
AND B J
AND C J
NOT J J
AND D J
WALK
"""

run = """OR A J
AND B J
AND C J
NOT J J
AND D J
OR E T
OR H T
AND T J
RUN
"""


def hull_damage(program, springscript, debug=False):
    cpu = intcode(program, *list(map(ord, springscript)))
    if debug:
        print(''.join(map(chr, cpu.outputs)))
    else:
        return cpu.outputs[-1]


def hull_damage_walk(program):
    return hull_damage(program, walk)


def hull_damage_run(program):
    return hull_damage(program, run)


if __name__ == "__main__":
    solve(21, parse, hull_damage_walk, hull_damage_run)
