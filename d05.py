#!/usr/bin/env python

"""Advent of Code 2019, Day 5"""

from aoc19 import solve

from intcode import intcode


def parse(data):
    return list(map(int, data.split(',')))


def air_conditioner(memory):
    return intcode(memory, 1).outputs[-1]


def thermal_radiator_controller(memory):
    return intcode(memory, 5).outputs[-1]


if __name__ == "__main__":
    solve(5, parse, air_conditioner, thermal_radiator_controller)
