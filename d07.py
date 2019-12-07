#!/usr/bin/env python

"""Advent of Code 2019, Day 7"""

from aoc19 import solve
from intcode import IntcodeCPU
from itertools import permutations


def parse(data):
    return list(map(int, data.split(',')))


def amplification_circuit(program, setting):
    amplifiers = [IntcodeCPU(program, s) for s in setting]

    # Process the initial input.
    for amplifier in amplifiers:
        amplifier.execute()

    # Run the feedback loop.
    signal = 0
    while amplifiers[0].waiting_for_input:
        for amplifier in amplifiers:
            amplifier.inputs.append(signal)
            amplifier.execute()
            signal = amplifier.outputs[-1]

    return signal


def max_signal(program, settings):
    return max(amplification_circuit(program, s) for s in settings)


def max_no_loop(program):
    return max_signal(program, permutations(range(5)))


def max_feedback_loop(program):
    return max_signal(program, permutations(range(5, 10)))


if __name__ == "__main__":
    solve(7, parse, max_no_loop, max_feedback_loop)
