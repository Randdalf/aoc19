#!/usr/bin/env python

"""Advent of Code 2019, Day 16"""

from aoc19 import solve


def parse(data):
    return list(map(int, data))


def gen_pattern(element):
    while True:
        for value in [0, 1, 0, -1]:
            for _ in range(element + 1):
                yield value


def fft(input, phases):
    for phase in range(phases):
        output = []
        for i, digit in enumerate(input):
            pattern = gen_pattern(i)
            next(pattern)
            output.append(abs(sum(d * p for d, p in zip(input, pattern))) % 10)
        input = output
    return ''.join(map(str, input[:8]))


if __name__ == "__main__":
    solve(16, parse, lambda i: fft(i, 100))
