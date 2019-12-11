#!/usr/bin/env python

"""Advent of Code 2019, Day 3"""

import math

from aoc19 import solve
from vec2 import Vec2


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
    wires = []
    for wire in data.split('\n'):
        sections = []
        for section in wire.split(','):
            sections.append((dirs[section[0]], int(section[1:])))
        wires.append(sections)
    return wires


def trace_wire(wire):
    trace = {}
    pos = Vec2(0, 0)
    steps = 0
    for dir, dist in wire:
        for i in range(dist):
            pos += dir
            steps += 1
            if pos not in trace:
                trace[pos] = steps
    return trace


def closest_intersection(wires):
    traces = [trace_wire(wire).keys() for wire in wires]
    intersections = traces[0] & traces[1]
    return min(dist(Vec2(0, 0), pt) for pt in intersections)


def fewest_steps_intersection(wires):
    traces = [trace_wire(wire) for wire in wires]
    intersections = traces[0].keys() & traces[1].keys()
    return min(traces[0][pt] + traces[1][pt] for pt in intersections)


if __name__ == "__main__":
    solve(3, parse, closest_intersection, fewest_steps_intersection)
