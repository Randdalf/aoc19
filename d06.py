#!/usr/bin/env python

"""Advent of Code 2019, Day 6"""

from collections import defaultdict
import math

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


def find_path(orbits, body, target, path):
    if body == target:
        return path

    path.append(body)
    for child in orbits[body]:
        result = find_path(orbits, child, target, path)
        if result:
            return result
    path.pop()


def orbital_transfers(orbits):
    you_path = find_path(orbits, 'COM', 'YOU', [])
    san_path = find_path(orbits, 'COM', 'SAN', [])

    needle = 0
    while you_path[needle] == san_path[needle]:
        needle += 1

    return len(san_path) + len(you_path) - 2 * needle


if __name__ == "__main__":
    solve(6, parse, orbit_count_checksum, orbital_transfers)
