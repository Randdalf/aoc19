#!/usr/bin/env python

"""Advent of Code 2019, Day 8"""

from collections import defaultdict
import math

from aoc19 import solve


def parse(data):
    return list(map(int, data))


def fewest_zero_digits(digits, width, height):
    layer_size = width * height
    fewest_zeros = math.inf
    result = None
    for start in range(0, len(digits), layer_size):
        totals = defaultdict(int)
        for d in digits[start:start+layer_size]:
            totals[d] += 1
        if not result or totals[0] < fewest_zeros:
            fewest_zeros = totals[0]
            result = totals[1] * totals[2]
    return result


def fewest_zero_digits_25_6(digits):
    return fewest_zero_digits(digits, 25, 6)


if __name__ == "__main__":
    solve(8, parse, lambda ds: fewest_zero_digits_25_6(ds))
