#!/usr/bin/env python

"""Advent of Code 2019, Day 10"""

from math import atan2

from aoc19 import solve


class Vec2:
    def __init__(slf, x, y):
        slf.x = x
        slf.y = y

    def __add__(slf, otr):
        return Vec2(slf.x + otr.x, slf.y + otr.y)

    def __sub__(slf, otr):
        return Vec2(slf.x - otr.x, slf.y - otr.y)

    def __hash__(slf):
        return hash(('Vec2', slf.x, slf.y))

    def __eq__(slf, otr):
        return slf.x == otr.x and slf.y == otr.y

    def __str__(slf):
        return f'({slf.x}, {slf.y})'


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


def best_location(asteroids):
    max = None
    for station in asteroids:
        views = set()
        for asteroid in asteroids:
            if station != asteroid:
                offset = asteroid - station
                views.add(round(atan2(offset.y, offset.x), 4))
        if max is None or len(views) > max:
            max = len(views)
    return max


if __name__ == "__main__":
    solve(10, parse, best_location)
