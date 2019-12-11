#!/usr/bin/env python

"""Advent of Code 2019, Day 11"""

from collections import defaultdict

from aoc19 import solve
from intcode import IntcodeCPU
from vec2 import Vec2


class DIR:
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class COLOR:
    BLACK = 0
    WHITE = 1


dirs = {
    DIR.UP: Vec2(0, 1),
    DIR.RIGHT: Vec2(1, 0),
    DIR.DOWN: Vec2(0, -1),
    DIR.LEFT: Vec2(-1, 0)
}


def parse(data):
    return list(map(int, data.split(',')))


def paint_panels(program):
    robot = IntcodeCPU(program)
    dir = DIR.UP
    pos = Vec2(0, 0)
    panels = defaultdict(lambda: COLOR.BLACK)

    robot.inputs.append(panels[pos])
    robot.execute()

    while robot.waiting_for_input:
        color, turn = robot.outputs[-2:]
        panels[pos] = color
        dir = (dir + 2 * turn - 1) % 4
        pos += dirs[dir]
        robot.inputs.append(panels[pos])
        robot.execute()

    return len(panels)


if __name__ == "__main__":
    solve(11, parse, paint_panels)
