#!/usr/bin/env python

"""Advent of Code 2019, Day 3"""

import math

from aoc19 import solve


class Vec2:
    def __init__(slf, x, y):
        slf.x = x
        slf.y = y

    def __add__(slf, otr):
        return Vec2(slf.x + otr.x, slf.y + otr.y)

    def __hash__(slf):
        return hash(('Vec2', slf.x, slf.y))

    def __eq__(slf, otr):
        return slf.x == otr.x and slf.y == otr.y

    def __str__(slf):
        return f'({slf.x}, {slf.y})'


def dist(a, b):
    return abs(a.x - b.x) + abs(a.y - b.y)


class DIR:
    UP = 'U'
    DOWN = 'D'
    LEFT = 'L'
    RIGHT = 'R'


dirs = {
    DIR.UP: Vec2(0, +1),
    DIR.DOWN: Vec2(0, -1),
    DIR.LEFT: Vec2(-1, 0),
    DIR.RIGHT: Vec2(+1, 0)
}


def parse(data):
    for wire in data.split('\n'):
        sections = []
        for section in wire.split(','):
            sections.append((dirs[section[0]], int(section[1:])))
        yield sections


def trace_wire(wire):
    trace = set()
    pos = Vec2(0, 0)
    for dir, dist in wire:
        for i in range(dist):
            pos += dir
            trace.add(pos)
    return trace


def closest_intersection(wires):
    central = Vec2(0, 0)
    traces = [trace_wire(wire) for wire in wires]
    intersections = traces[0] & traces[1]
    return min(dist(central, pt) for pt in intersections)


if __name__ == "__main__":
    solve(3, parse, closest_intersection)
