#!/usr/bin/env python

"""Advent of Code 2019, Day 2"""

from itertools import product

from aoc19 import solve
from intcode import IntcodeCPU


def parse(data):
    return list(map(int, data.split(',')))


def program_override(program, noun, verb):
    cpu = IntcodeCPU(program)
    cpu.memory[1] = noun
    cpu.memory[2] = verb
    cpu.execute()
    return cpu.memory[0]


def program_alarm_1202(program):
    return program_override(program, 12, 2)


def gravity_assist(program):
    for noun, verb in product(range(100), range(100)):
        if program_override(program, noun, verb) == 19690720:
            return 100 * noun + verb


if __name__ == "__main__":
    solve(2, parse, program_alarm_1202, gravity_assist)
