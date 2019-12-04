#!/usr/bin/env python

"""Advent of Code 2019, Day 4"""

from aoc19 import solve


def parse(data):
    return tuple(map(int, data.split('-')))


def is_password(number):
    digits = [int(d) for d in str(number)]
    has_double = False
    for i in range(len(digits)-1):
        d0 = digits[i]
        d1 = digits[i+1]
        has_double |= d0 == d1
        if d0 > d1:
            return False
    return has_double


def is_true_password(number):
    digits = [int(d) for d in str(number)]

    for i in range(len(digits)-1):
        if digits[i] > digits[i+1]:
            return False

    prev = None
    count = 0
    for d in digits:
        if d == prev:
            count += 1
        else:
            if count == 2:
                return True
            prev = d
            count = 1

    return count == 2


def num_passwords(data):
    return len([n for n in range(*data) if is_password(n)])


def num_true_passwords(data):
    return len([n for n in range(*data) if is_true_password(n)])


if __name__ == "__main__":
    solve(4, parse, num_passwords, num_true_passwords)
