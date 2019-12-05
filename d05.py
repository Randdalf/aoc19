#!/usr/bin/env python

"""Advent of Code 2019, Day 5"""

from aoc19 import solve

from intcode import IntcodeComputer


def parse(data):
    return list(map(int, data.split(',')))


def air_conditioner(memory):
    cpu = IntcodeComputer(memory)
    cpu.execute(1)
    return cpu.outputs[-1]


if __name__ == "__main__":
    solve(5, parse, test_diagnostic)
