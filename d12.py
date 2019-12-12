#!/usr/bin/env python

"""Advent of Code 2019, Day 12"""

from itertools import combinations
import re

from aoc19 import solve


class Vec3:
    def __init__(slf, x, y, z):
        slf.x = x
        slf.y = y
        slf.z = z

    def __add__(slf, otr):
        return Vec3(slf.x + otr.x, slf.y + otr.y, slf.z + otr.z)

    def __sub__(slf, otr):
        return Vec3(slf.x - otr.x, slf.y - otr.y, slf.z - otr.z)

    def __getitem__(slf, axis):
        return slf.values[axis]

    def __str__(slf):
        return f'<x={slf.x}, y={slf.y}, z={slf.z}>'


class Moon:
    def __init__(slf, x, y, z):
        slf.pos = Vec3(x, y, z)
        slf.vel = Vec3(0, 0, 0)

    @property
    def energy(slf):
        potential = abs(slf.pos.x) + abs(slf.pos.y) + abs(slf.pos.z)
        kinetic = abs(slf.vel.x) + abs(slf.vel.y) + abs(slf.vel.z)
        return potential * kinetic

    def __str__(slf):
        return f'pos={slf.pos}, vel={slf.vel}'


def parse(data):
    pattern = re.compile(r"<x=(-?\d+), y=(-?\d+), z=(-?\d+)>")
    lines = data.split('\n')
    matches = [re.match(pattern, line) for line in lines]
    return [Moon(*map(int, match.groups())) for match in matches]


def pull(a, b):
    return int(a < b) - int(a > b)


def simulate(moons, steps):
    pairs = list(combinations(moons, 2))
    for step in range(steps):
        for a, b in pairs:
            pull_x = pull(a.pos.x, b.pos.x)
            pull_y = pull(a.pos.y, b.pos.y)
            pull_z = pull(a.pos.z, b.pos.z)
            offset = Vec3(pull_x, pull_y, pull_z)
            a.vel += offset
            b.vel -= offset
        for moon in moons:
            moon.pos += moon.vel


def total_energy(moons, steps):
    simulate(moons, steps)
    return sum(moon.energy for moon in moons)


def total_energy_1000(moons):
    return total_energy(moons, 1000)


if __name__ == "__main__":
    solve(12, parse, total_energy_1000)
