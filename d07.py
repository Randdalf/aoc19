#!/usr/bin/env python

"""Advent of Code 2019, Day 7"""

from aoc19 import solve
from intcode import intcode
from itertools import permutations


def parse(data):
    return list(map(int, data.split(',')))


def amplification_circuit(program, setting):
    input = 0
    for amp in range(5):
        input = intcode(program, setting[amp], input).outputs[-1]
    return input


def max_thruster_signal(program):
    settings = permutations(range(5))
    return max(amplification_circuit(program, s) for s in settings)


if __name__ == "__main__":
    solve(7, parse, max_thruster_signal)
