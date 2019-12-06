#!/usr/bin/env python

"""Advent of Code 2019, Day 6"""

from collections import defaultdict

from aoc19 import solve


def parse(data):
    orbits = defaultdict(list)
    for orbit in data.split('\n'):
        a, b = orbit.split(')')
        orbits[a].append(b)
    return orbits


def total_orbits(orbits, body, depth=0):
    return depth + sum(total_orbits(orbits, b, depth+1) for b in orbits[body])


def orbit_count_checksum(orbits, depth=0):
    return total_orbits(orbits, 'COM')


if __name__ == "__main__":
    solve(6, parse, orbit_count_checksum)
