#!/usr/bin/env python

"""Advent of Code 2019, Day 2"""

from itertools import product

from aoc19 import solve


class OPCODE:
    ADD = 1
    MULTPLY = 2
    STOP = 99


ops = {
    OPCODE.ADD: lambda x, y: x + y,
    OPCODE.MULTPLY: lambda x, y: x * y
}


def parse(data):
    return list(map(int, data.split(',')))


def intpoint(program):
    pc = 0
    while program[pc] != OPCODE.STOP:
        op = program[pc]
        left = program[program[pc+1]]
        right = program[program[pc+2]]
        out = program[pc+3]
        program[out] = ops[op](left, right)
        pc += 4
    return program[0]


def program_alarm_1202(program):
    program[1] = 12
    program[2] = 2
    return intpoint(program)


def gravity_assist(program):
    for noun, verb in product(range(100), range(100)):
        clone = list(program)
        clone[1] = noun
        clone[2] = verb
        if intpoint(clone) == 19690720:
            return 100 * noun + verb


if __name__ == "__main__":
    solve(2, parse, program_alarm_1202, gravity_assist)
