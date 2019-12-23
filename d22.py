#!/usr/bin/env python

"""Advent of Code 2019, Day 22"""

from aoc19 import solve


class TECHNIQUE:
    CUT = 'cut'
    DEAL = 'deal with increment'
    NEW = 'deal into new stack'


def parse(data):
    commands = []
    for line in data.split('\n'):
        if line == TECHNIQUE.NEW:
            commands.append((TECHNIQUE.NEW,))
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


def flatten(commands, n):
    coeff = 1
    shift = 0
    for command in reversed(commands):
        if command[0] == TECHNIQUE.NEW:
            shift = n - 1 - shift
            coeff *= -1
        elif command[0] == TECHNIQUE.CUT:
            shift += n + command[1] if command[1] < 0 else command[1]
        elif command[0] == TECHNIQUE.DEAL:
            inv = mod_inverse(command[1], n)
            shift *= inv
            coeff *= inv
    return coeff, shift


def shuffled(commands, n):
    coeff, shift = flatten(commands, n)
    return [(coeff*i + shift) % n for i in range(n)]


def shuffled_index(commands, n=10007, card=2019):
    return shuffled(commands, n).index(card)


if __name__ == "__main__":
    solve(22, parse, shuffled_index)
