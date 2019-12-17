#!/usr/bin/env python

"""Advent of Code 2019, Day 17"""

from itertools import product, repeat

from aoc19 import solve
from intcode import intcode, IntcodeCPU
from vec2 import Vec2


class TILE:
    EMPTY = '.'
    SCAFFOLD = '#'
    LEFT = '<'
    RIGHT = '>'
    UP = '^'
    DOWN = 'v'


class INPUT:
    LEFT = 'L'
    RIGHT = 'R'
    A = 'A'
    B = 'B'
    C = 'C'
    NO = 'n'


dirs = {
    TILE.LEFT: Vec2(-1, 0),
    TILE.RIGHT: Vec2(+1, 0),
    TILE.UP: Vec2(0, -1),
    TILE.DOWN: Vec2(0, +1)
}

order = [
    Vec2(0, -1),
    Vec2(1, 0),
    Vec2(0, 1),
    Vec2(-1, 0)
]


def parse(data):
    return list(map(int, data.split(',')))


def select_dir(pos, view, visited):
    for dir in dirs.values():
        next = pos + dir
        if next not in visited and next in view:
            if view[next] == TILE.SCAFFOLD:
                return dir


def rotate(from_dir, to_dir):
    n = len(order)
    from_index = order.index(from_dir)
    to_index = order.index(to_dir)
    right_dist = (to_index - from_index) % n
    left_dist = (from_index - to_index + n) % n
    if left_dist < right_dist:
        return repeat(INPUT.LEFT, left_dist)
    else:
        return repeat(INPUT.RIGHT, right_dist)


def find_path(program, display=False):
    x = 0
    y = 0
    view = {}
    for tile in map(chr, intcode(program).outputs):
        if tile == '\n':
            x = 0
            y += 1
        else:
            pos = Vec2(x, y)
            view[pos] = tile
            if tile in dirs.keys():
                start = pos
                facing = dirs[tile]
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

    visited = set()
    path = []
    moves = []
    pos = start
    dir = select_dir(pos, view, visited)
    while dir:
        next = pos + dir
        moves.extend(rotate(facing, dir))
        facing = dir
        n = 0
        while next in view and view[next] == TILE.SCAFFOLD:
            visited.add(pos)
            path.append(pos)
            pos = next
            next += dir
            n += 1
        moves.append(str(n))
        dir = select_dir(pos, view, visited)

    return path, moves


def alignment_parameters(program):
    path, moves = find_path(program)
    visited = set()
    intersections = set()
    for pos in path:
        if pos in visited:
            intersections.add(pos)
        else:
            visited.add(pos)
    return sum(p.x * p.y for p in intersections)


def space_dust(program):
    path, moves = find_path(program)

    for an, bn, cn in product(range(1, 11), range(1, 11), range(1, 11)):
        main = []
        offset = 0

        # Select A and find its initial repetitions.
        a = moves[offset:offset+an]
        while offset < len(moves):
            if moves[offset:offset+an] == a:
                main.append(INPUT.A)
                offset += an
            else:
                break

        # Select B and find repetitions of A and B.
        b = moves[offset:offset+bn]
        while offset < len(moves):
            if moves[offset:offset+an] == a:
                main.append(INPUT.A)
                offset += an
            elif moves[offset:offset+bn] == b:
                main.append(INPUT.B)
                offset += bn
            else:
                break

        # Select C and find repetitions of A, B and C.
        c = moves[offset:offset+cn]
        while offset < len(moves):
            if moves[offset:offset+an] == a:
                main.append(INPUT.A)
                offset += an
            elif moves[offset:offset+bn] == b:
                main.append(INPUT.B)
                offset += bn
            elif moves[offset:offset+cn] == c:
                main.append(INPUT.C)
                offset += cn
            else:
                break

        # We found our functions if we perfectly match the move list.
        if offset == len(moves):
            input = ','.join(main) + '\n'
            input += ','.join(a) + '\n'
            input += ','.join(b) + '\n'
            input += ','.join(c) + '\n'
            input += INPUT.NO + '\n'
            robot = IntcodeCPU(program, *list(map(ord, input)))
            robot.memory[0] = 2
            robot.execute()
            return robot.outputs[-1]


if __name__ == "__main__":
    solve(17, parse, alignment_parameters, space_dust)
