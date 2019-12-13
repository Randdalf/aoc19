#!/usr/bin/env python

"""Advent of Code 2019, Day 13"""

from collections import defaultdict
import os

from aoc19 import solve
from intcode import intcode, IntcodeCPU, disassemble
from vec2 import Vec2


class TILE:
    EMPTY = 0
    WALL = 1
    BLOCK = 2
    PADDLE = 3
    BALL = 4


class JOYSTICK:
    LEFT = -1
    NEUTRAL = 0
    RIGHT = 1


def parse(data):
    return list(map(int, data.split(',')))


def num_block_tiles(game):
    cabinet = intcode(game)
    screen = {}
    for i in range(0, len(cabinet.outputs), 3):
        x, y, tile = cabinet.outputs[i:i+3]
        screen[Vec2(x, y)] = tile
    return len([tile for tile in screen.values() if tile == TILE.BLOCK])


def play_game(game, display=False, cpu=True):
    cabinet = IntcodeCPU(game)
    cabinet.memory[0] = 2
    screen = defaultdict(lambda: TILE.EMPTY)
    score = 0
    num_blocks = num_block_tiles(game)
    paddle = None
    ball = None

    while num_blocks > 0:
        cabinet.execute()
        for i in range(0, len(cabinet.outputs), 3):
            x, y, tile = cabinet.outputs[i:i+3]
            if x == -1 and y == 0:
                score = tile
            else:
                pos = Vec2(x, y)
                if screen[pos] == TILE.BLOCK and tile == TILE.EMPTY:
                    num_blocks -= 1
                screen[pos] = tile
                if tile == TILE.PADDLE:
                    paddle = x
                elif tile == TILE.BALL:
                    ball = x

        cabinet.outputs.clear()

        if display:
            os.system('clear')
            width = 1 + max(v.x for v in screen.keys())
            height = 1 + max(v.y for v in screen.keys())

            for y in range(height):
                row = ''
                for x in range(width):
                    row += ' |#_o'[screen[Vec2(x, y)]]
                print(row)

        if cpu:
            if paddle < ball:
                cabinet.inputs.append(JOYSTICK.RIGHT)
            elif paddle > ball:
                cabinet.inputs.append(JOYSTICK.LEFT)
            else:
                cabinet.inputs.append(JOYSTICK.NEUTRAL)
        else:
            joystick = None
            while joystick is None:
                try:
                    joystick = int(input('Joystick [-1, 0, 1]:'))
                except ValueError:
                    pass
            cabinet.inputs.append(joystick)

    return score


if __name__ == "__main__":
    solve(13, parse, num_block_tiles, play_game)
