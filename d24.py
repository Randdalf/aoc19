#!/usr/bin/env python

"""Advent of Code 2019, Day 24"""

from collections import defaultdict, deque
from itertools import product

from aoc19 import solve


class TILE:
    BUG = '#'
    EMPTY = '.'
    RECURSIVE = '?'


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
            elif tile == TILE.EMPTY and 1 <= bugs <= 2:
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


def adjacencies(x, y, level):
    # North
    north = y - 1
    if north == -1:
        yield (2, 1, level-1)
    elif x == 2 and north == 2:
        for ax in range(5):
            yield (ax, 4, level+1)
    else:
        yield (x, north, level)

    # South
    south = y + 1
    if south == 5:
        yield (2, 3, level-1)
    elif x == 2 and south == 2:
        for ax in range(5):
            yield (ax, 0, level+1)
    else:
        yield (x, south, level)

    # West
    west = x - 1
    if west == -1:
        yield (1, 2, level-1)
    elif west == 2 and y == 2:
        for ay in range(5):
            yield (4, ay, level+1)
    else:
        yield (west, y, level)

    # East
    east = x + 1
    if east == 5:
        yield (3, 2, level-1)
    elif east == 2 and y == 2:
        for ay in range(5):
            yield (0, ay, level+1)
    else:
        yield (east, y, level)


def print_irg(irg):
    min_depth = min(level for x, y, level in irg.keys())
    max_depth = max(level for x, y, level in irg.keys())

    for depth in range(min_depth, max_depth+1):
        if depth == min_depth:
            print(f'Depth {depth}:')
        else:
            print(f'\nDepth {depth}:')
        for y in range(5):
            row = ''
            for x in range(5):
                if x == 2 and y == 2:
                    row += '?'
                else:
                    row += irg[(x, y, depth)]
            print(row)


def recursive_bugs(grid, minutes=200, display=False):
    irg = defaultdict(
        lambda: TILE.EMPTY,
        {(x, y, 0): tile for (x, y), tile in grid.items()}
    )
    irg[(2, 2, 0)] = TILE.RECURSIVE

    for minute in range(minutes):
        new_irg = defaultdict(lambda: TILE.EMPTY)

        # Add all bug tiles, and tiles adjacent to bug tiles, for processing.
        pending = set()
        for key, tile in irg.items():
            if tile == TILE.BUG:
                pending.add(key)
                pending.update(adjacencies(*key))

        # Process all the interesting tiles.
        while len(pending) > 0:
            key = pending.pop()
            tile = irg[key]
            bugs = sum(int(irg[adj] == TILE.BUG) for adj in adjacencies(*key))
            if tile == TILE.BUG and bugs != 1:
                new_irg[key] = TILE.EMPTY
            elif tile == TILE.EMPTY and 1 <= bugs <= 2:
                new_irg[key] = TILE.BUG
            else:
                new_irg[key] = tile

        # Switch to the updated grid.
        irg = new_irg

    if display:
        print_irg(irg)

    return list(irg.values()).count(TILE.BUG)


if __name__ == "__main__":
    solve(24, parse, biodiversity_rating, recursive_bugs)
