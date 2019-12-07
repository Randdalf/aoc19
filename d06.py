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


def path_from_com(parents, body):
    path = []
    while body != 'COM':
        path.append(body)
        body = parents[body]
    path.reverse()
    return path


def orbital_transfers(orbits):
    parents = {}
    for parent, children in orbits.items():
        for child in children:
            parents[child] = parent

    you_path = path_from_com(parents, 'YOU')
    san_path = path_from_com(parents, 'SAN')

    needle = 0
    while you_path[needle] == san_path[needle]:
        needle += 1

    return len(san_path) + len(you_path) - 2 * (needle + 1)


if __name__ == "__main__":
    solve(6, parse, orbit_count_checksum, orbital_transfers)
