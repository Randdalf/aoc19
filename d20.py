#!/usr/bin/env python

"""Advent of Code 2019, Day 20"""

from collections import defaultdict

from aoc19 import solve
from pathfind import dijkstra, path_length
from vec2 import Vec2


class TILE:
    EMPTY = ' '
    PASSAGE = '.'
    WALL = '#'


class DonutMaze:
    def __init__(slf, adjacencies, labels, portals, inner, outer):
        slf.adjacencies = adjacencies
        slf.labels = labels
        slf.portals = portals
        slf.inner = inner
        slf.outer = outer
        slf.edge = inner | outer


class Node:
    def __init__(slf, maze, pos):
        slf.maze = maze
        slf.pos = pos
        slf.hash = hash(pos)

    def __hash__(slf):
        return slf.hash

    def __eq__(slf, otr):
        # Risky optimisation.
        return slf.hash == otr.hash

    @property
    def neighbors(slf):
        for adj in slf.maze.adjacencies[slf.pos]:
            yield Node(slf.maze, adj)

    def dist(slf, neighbor):
        return 1


class RecNode:
    def __init__(slf, maze, pos, level):
        slf.maze = maze
        slf.pos = pos
        slf.level = level
        slf.hash = hash((pos, level))

    def __hash__(slf):
        return slf.hash

    def __eq__(slf, otr):
        # Risky optimisation.
        return slf.hash == otr.hash

    @property
    def neighbors(slf):
        for adj in slf.maze.adjacencies[slf.pos]:
            if slf.pos in slf.maze.edge and adj in slf.maze.edge:
                if adj in slf.maze.inner and slf.level > 0:
                    yield RecNode(slf.maze, adj, slf.level - 1)
                elif adj in slf.maze.outer:
                    yield RecNode(slf.maze, adj, slf.level + 1)
            else:
                yield RecNode(slf.maze, adj, slf.level)

    def dist(slf, neighbor):
        return 1


dirs = [
    Vec2(0, -1),
    Vec2(1, 0),
    Vec2(0, 1),
    Vec2(-1, 0)
]


def parse(data):
    tiles = {}
    for y, row in enumerate(data.split('\n')):
        for x, tile in enumerate(row):
            tiles[Vec2(x, y)] = tile

    adjacencies = defaultdict(list)
    labels = {}
    portals = defaultdict(list)
    for pos, tile in tiles.items():
        if tile == TILE.PASSAGE:
            for dir in dirs:
                adj = pos + dir
                if tiles[adj].isupper():
                    label = tiles[adj] + tiles[adj+dir]
                    if dir.x < 0 or dir.y < 0:
                        label = label[1] + label[0]
                    portals[label].append(pos)
                    labels[pos] = label
                elif tiles[adj] == TILE.PASSAGE:
                    adjacencies[pos].append(adj)

    for pos, tile in tiles.items():
        if tile == TILE.PASSAGE and pos in labels:
            teleports = portals[labels[pos]]
            adjacencies[pos].extend(t for t in teleports if t != pos)

    w = 1 + max(pos.x for pos in tiles.keys())
    h = 1 + max(pos.y for pos in tiles.keys())
    inner = set()
    outer = set()
    for pos, tile in tiles.items():
        if pos in labels:
            if pos.x == 2 or pos.y == 2 or pos.x == w - 3 or pos.y == h - 3:
                outer.add(pos)
            else:
                inner.add(pos)

    return DonutMaze(adjacencies, labels, portals, inner, outer)


def aa_to_zz(maze):
    start = Node(maze, maze.portals['AA'][0])
    end = Node(maze, maze.portals['ZZ'][0])

    def goal(node):
        return node == end

    return path_length(dijkstra(start, goal))


def aa_to_zz_recursive(maze):
    start = RecNode(maze, maze.portals['AA'][0], 0)
    end = RecNode(maze, maze.portals['ZZ'][0], 0)

    def goal(node):
        return node == end

    return path_length(dijkstra(start, goal))


if __name__ == "__main__":
    solve(20, parse, aa_to_zz, aa_to_zz_recursive)
