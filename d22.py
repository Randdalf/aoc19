#!/usr/bin/env python

"""Advent of Code 2019, Day 22"""

from itertools import repeat

from aoc19 import solve


class TECHNIQUE:
    CUT = 'cut'
    DEAL = 'deal with increment'
    REVERSE = 'deal into new stack'


def parse(data):
    commands = []
    for line in data.split('\n'):
        if line == TECHNIQUE.REVERSE:
            commands.append((TECHNIQUE.REVERSE,))
        elif line.startswith(TECHNIQUE.CUT):
            cut = int(line.replace(TECHNIQUE.CUT, '').strip())
            commands.append((TECHNIQUE.CUT, cut))
        elif line.startswith(TECHNIQUE.DEAL):
            step = int(line.replace(TECHNIQUE.DEAL, '').strip())
            commands.append((TECHNIQUE.DEAL, step))
    return commands


def mod_inverse(a, n):
    s = 0
    old_s = 1
    r = n
    old_r = a
    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
    return old_s % n


def flattened(commands, n):
    coeff = 1
    shift = 0
    for command in reversed(commands):
        if command[0] == TECHNIQUE.REVERSE:
            shift = n - 1 - shift
            coeff *= -1
        elif command[0] == TECHNIQUE.CUT:
            shift += n + command[1] if command[1] < 0 else command[1]
        elif command[0] == TECHNIQUE.DEAL:
            inv = mod_inverse(command[1], n)
            shift *= inv
            coeff *= inv
    return coeff % n, shift % n


def inverted(commands, n):
    coeff = 1
    shift = 0
    for command in commands:
        if command[0] == TECHNIQUE.REVERSE:
            shift = n - 1 - shift
            coeff *= -1
        elif command[0] == TECHNIQUE.CUT:
            shift += -command[1] if command[1] < 0 else n - command[1]
        elif command[0] == TECHNIQUE.DEAL:
            shift *= command[1]
            coeff *= command[1]
    return coeff % n, shift % n


def shuffle(commands, n=119315717514047, iters=101741582076661, index=2020):
    a, b = flattened(commands, n)

    if iters == 1:
        return (a*index + b) % n

    # Explanation:
    #     1 shuffle:  (a*x + b) % n
    #     2 shuffles: (a^2*x + b*a + b) % n
    #     3 shuffles: (a^3*x + b*a^2 + b*a + b) % n
    #     t shuffles: (a^t*x + b*(a^(t-1) + a^(t-2) + ... + a^ 1 + a^0)) % n
    #
    # (a^t) % n can be efficiently computed using pow(a, t, n).
    #
    # The series is a geometric series which can be rewritten as:
    #     geom(b, a, t) = b * (1 - a^t) / (1 - a)
    #
    # But under modulo, division is the modular inverse.
    #     geom(b, a, t) % n = (b * (1 - a^t) * mod_inverse(1 - a, n)) % n
    #
    # Putting it all together:
    a_t = pow(a, iters, n)
    return (a_t * index + b * (1 - a_t) * mod_inverse(1 - a, n)) % n


def unshuffle(commands, n=10007, card=2019):
    a, b = inverted(commands, n)
    return (a*card + b) % n


if __name__ == "__main__":
    solve(22, parse, unshuffle, shuffle)
