#!/usr/bin/env python

"""Advent of Code 2019, Day 4"""

from aoc19 import solve


def parse(data):
    return tuple(map(int, data.split('-')))


def is_password(number):
    digits = [int(d) for d in str(number)]
    has_double = False
    never_decreases = True
    for i in range(len(digits)-1):
        d0 = digits[i]
        d1 = digits[i+1]
        has_double |= d0 == d1
        if d0 > d1:
            return False
    return has_double


def num_passwords(data):
    return len(list(n for n in range(*data) if is_password(n)))


if __name__ == "__main__":
    solve(4, parse, num_passwords)
