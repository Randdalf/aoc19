#!/usr/bin/env python

"""Advent of Code 2019, Day 17"""

from aoc19 import solve
from intcode import intcode
from vec2 import Vec2


class TILE:
    EMPTY = '.'
    SCAFFOLD = '#'
    LEFT = '<'
    RIGHT = '>'
    UP = '^'
    DOWN = 'v'
    TUMBLING = 'X'
    NEWLINE = '\n'


dirs = {
    TILE.LEFT: Vec2(-1, 0),
    TILE.RIGHT: Vec2(+1, 0),
    TILE.UP: Vec2(0, -1),
    TILE.DOWN: Vec2(0, +1)
}


def parse(data):
    return list(map(int, data.split(',')))


def alignment_parameters(program, display=False):
    x = 0
    y = 0
    view = {}
    for tile in map(chr, intcode(program).outputs):
        if tile == TILE.NEWLINE:
            x = 0
            y += 1
        else:
            pos = Vec2(x, y)
            view[pos] = tile
            if tile in dirs.keys():
                start = pos
                dir = tile
            x += 1

    if display:
        width = 1 + max(p.x for p in view.keys())
        height = 1 + max(p.y for p in view.keys())
        for y in range(height):
            row = ''
            for x in range(width):
                row += view[Vec2(x, y)]
            print(row)

    def select_dir(pos, view, visited):
        for dir in dirs.values():
            next = pos + dir
            if next not in visited and next in view:
                if view[next] == TILE.SCAFFOLD:
                    return dir

    visited = set()
    intersections = set()
    pos = start
    dir = select_dir(pos, view, visited)
    while dir:
        while (pos + dir) in view and view[(pos + dir)] == TILE.SCAFFOLD:
            if pos in visited:
                intersections.add(pos)
            else:
                visited.add(pos)
            pos += dir
        dir = select_dir(pos, view, visited)

    return sum(p.x * p.y for p in intersections)


if __name__ == "__main__":
    solve(17, parse, alignment_parameters)
