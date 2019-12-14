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


if __name__ == "__main__":
    solve(14, parse, minimum_ore)
