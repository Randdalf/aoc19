#!/usr/bin/env python

"""Advent of Code 2019, Day 13"""

from aoc19 import solve
from intcode import intcode
from vec2 import Vec2


class TILE:
    EMPTY = 0
    WALL = 1
    BLOCK = 2
    PADDLE = 3
    BALL = 4


def parse(data):
    return list(map(int, data.split(',')))


def num_block_tiles(game):
    cabinet = intcode(game)
    screen = {}
    for i in range(0, len(cabinet.outputs), 3):
        x, y, tile = cabinet.outputs[i:i+3]
        screen[Vec2(x, y)] = tile
    return len([tile for tile in screen.values() if tile == TILE.BLOCK])


if __name__ == "__main__":
    solve(13, parse, num_block_tiles)
