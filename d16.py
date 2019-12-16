#!/usr/bin/env python

"""Advent of Code 2019, Day 16"""

from itertools import cycle, islice

from aoc19 import solve


def parse(data):
    return list(map(int, data))


def chunked(input, size, num, offset):
    for i in range(0, len(input), size * num_chunks):
        yield from input[i:i+size]


def chunked(input, size, index, num, offset):
    for i in range(index * size + offset, len(input), size * num):
        yield from input[i:i+size]


def fft(input, phases=100):
    for phase in range(phases):
        output = []
        for i, digit in enumerate(input):
            size = i + 1
            pos = sum(chunked(input, size, 1, 4, -1))
            neg = sum(chunked(input, size, 3, 4, -1))
            output.append(abs(pos - neg) % 10)
        input = output
    return ''.join(map(str, input[:8]))


def real_signal(input, phases=100):
    offset = int(''.join(map(str, input[:7])))
    signal = list(islice(cycle(input), offset, 10000 * len(input)))
    n = len(signal)
    for phase in range(phases):
        for i in reversed(range(n-1)):
            signal[i] += signal[i+1]
    return ''.join(str(d % 10) for d in signal[:8])


if __name__ == "__main__":
    solve(16, parse, fft, real_signal)
