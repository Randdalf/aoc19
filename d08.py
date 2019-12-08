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


def decode_image(digits, width, height):
    size = width * height
    image = [2 for i in range(size)]
    for start in range(0, len(digits), size):
        for i, d in enumerate(digits[start:start+size]):
            if image[i] == 2:
                image[i] = d
    pixels = [' # '[d] for d in image]
    rows = [''.join(pixels[i:i+width]) for i in range(0, size, width)]
    return '\n'.join(rows)


def fewest_zero_digits_25_6(digits):
    return fewest_zero_digits(digits, 25, 6)


def decode_image_25_6(digits):
    return decode_image(digits, 25, 6)


if __name__ == "__main__":
    solve(8, parse, fewest_zero_digits_25_6, decode_image_25_6)
