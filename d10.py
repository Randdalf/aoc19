#!/usr/bin/env python

"""Advent of Code 2019, Day 10"""

from collections import defaultdict
from math import atan2

from aoc19 import solve


class Vec2:
    def __init__(slf, x, y):
        slf.x = x
        slf.y = y

    def __sub__(slf, otr):
        return Vec2(slf.x - otr.x, slf.y - otr.y)

    def __hash__(slf):
        return hash(('Vec2', slf.x, slf.y))

    def __eq__(slf, otr):
        return slf.x == otr.x and slf.y == otr.y

    def __str__(slf):
        return f'({slf.x}, {slf.y})'

    def __repr__(slf):
        return f'Vec2({slf.x}, {slf.y})'

    def sqlength(slf):
        return slf.x * slf.x + slf.y * slf.y


def parse(data):
    rows = data.split('\n')
    height = len(rows)
    width = len(rows[0])
    asteroids = []
    for y in range(height):
        for x in range(width):
            if rows[y][x] == '#':
                asteroids.append(Vec2(x, y))
    return asteroids


def angle(v):
    return round(atan2(v.y, v.x), 3)


def map_asteroids(asteroids, station):
    mapped = defaultdict(list)
    for asteroid in asteroids:
        if station != asteroid:
            offset = asteroid - station
            mapped[angle(offset)].append(asteroid)
    return mapped


def best_location(asteroids):
    return max(len(map_asteroids(asteroids, s).keys()) for s in asteroids)


def vaporized_200(asteroids):
    maps = {s: map_asteroids(asteroids, s) for s in asteroids}
    station = max(maps.keys(), key=lambda x: len(maps[x].keys()))
    world = list(maps[station].items())

    # Sort the world by angle.
    world.sort(key=lambda x: x[0])

    # Sort each angle's asteroids by distance from the station. Reversed so we
    # can pop from the end of each array to vaporize an asteroid.
    for _, asteroids in world:
        asteroids.sort(key=lambda x: (x - station).sqlength(), reverse=True)

    # Find the index closest to the up angle.
    up = angle(Vec2(0, -1))
    index = 0
    while world[index][0] < up:
        index += 1

    # Vaporize!
    vaporized = []
    while len(vaporized) < 200:
        asteroids = world[index][1]
        if len(asteroids) > 0:
            vaporized.append(asteroids.pop())
        index = (index + 1) % len(world)

    # Return the 200th vaporized asteroid.
    coord = vaporized[-1]
    return coord.x * 100 + coord.y


if __name__ == "__main__":
    solve(10, parse, best_location, vaporized_200)
