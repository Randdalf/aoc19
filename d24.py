#!/usr/bin/env python

"""Advent of Code 2019, Day 24"""

from collections import defaultdict
from itertools import product

from aoc19 import solve


class TILE:
    BUG = '#'
    EMPTY = '.'


def parse(data):
    grid = defaultdict(lambda: TILE.EMPTY)
    for y, row in enumerate(data.split('\n')):
        for x, tile in enumerate(row):
            grid[(x, y)] = tile
    return grid


def print_grid(grid, minute):
    if minute == 0:
        print('Initial state:')
    elif minute == 1:
        print('\nAfter 1 minute:')
    else:
        print(f'\nAfter {minute} minutes:')

    for y in range(5):
        row = ''
        for x in range(5):
            row += grid[(x, y)]
        print(row)


def biodiversity_rating(grid, display=False):
    seen = set()
    signature = tuple(grid[(x, y)] for y, x in product(range(5), range(5)))
    minute = 0

    if display:
        print_grid(grid, minute)

    while signature not in seen:
        seen.add(signature)
        signature = []
        new_grid = defaultdict(lambda: TILE.EMPTY)
        for y, x in product(range(5), range(5)):
            bugs = int(grid[(x, y-1)] == TILE.BUG)
            bugs += int(grid[(x+1, y)] == TILE.BUG)
            bugs += int(grid[(x, y+1)] == TILE.BUG)
            bugs += int(grid[(x-1, y)] == TILE.BUG)
            tile = grid[(x, y)]
            if tile == TILE.BUG and bugs != 1:
                new_grid[(x, y)] = TILE.EMPTY
            elif tile == TILE.EMPTY and bugs >= 1 and bugs <= 2:
                new_grid[(x, y)] = TILE.BUG
            else:
                new_grid[(x, y)] = tile
            signature.append(new_grid[(x, y)])

        grid = new_grid
        signature = tuple(signature)
        minute += 1

        if display:
            print_grid(grid, minute)

    rating = 0
    for i, (y, x) in enumerate(product(range(5), range(5))):
        if grid[(x, y)] == TILE.BUG:
            rating += pow(2, i)
    return rating


if __name__ == "__main__":
    solve(24, parse, biodiversity_rating)
