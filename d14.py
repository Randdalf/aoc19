#!/usr/bin/env python

"""Advent of Code 2019, Day 14"""

from collections import defaultdict
from math import ceil

from aoc19 import solve


def parse(data):
    def parse_chem(s):
        units, name = s.split(' ')
        return int(units), name

    reactions = {}
    for reaction in data.split('\n'):
        input, output = reaction.split(' => ')
        inputs = []
        for chem in input.split(', '):
            inputs.append(parse_chem(chem))
        out_units, out_chem = parse_chem(output)
        reactions[out_chem] = (out_units, inputs)
    return reactions


def minimum_ore(reactions, chem='FUEL', units=1, waste=None):
    if waste is None:
        waste = defaultdict(int)

    if chem == 'ORE':
        return units

    # Re-use waste chemicals.
    reuse = min(units, waste[chem])
    units -= reuse
    waste[chem] -= reuse

    # Work out how many reactions we need to perform.
    produced, inputs = reactions[chem]
    n = ceil(units / produced)

    # Determine the minimum ore required to produce each input.
    ore = 0
    for required, input in inputs:
        ore += minimum_ore(reactions, input, n * required, waste)

    # Store waste so it can be re-used
    waste[chem] += n * produced - units

    return ore


def maximum_fuel(reactions):
    target = 1000000000000
    lower = None
    upper = 1

    # Find upper bound.
    while minimum_ore(reactions, units=upper) < target:
        lower = upper
        upper *= 2

    # Binary search to find
    while lower + 1 < upper:
        mid = (lower + upper) // 2
        ore = minimum_ore(reactions, units=mid)
        if ore > target:
            upper = mid
        elif ore < target:
            lower = mid

    return lower


if __name__ == "__main__":
    solve(14, parse, minimum_ore, maximum_fuel)
