#!/usr/bin/env python

"""Advent of Code 2019, Day 20"""

from collections import defaultdict
import math
from pqueue import pqueue

from aoc19 import solve
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
        slf.teleports = inner | outer


class Node:
    def __init__(slf, pos):
        slf.pos = pos
        slf.hash = hash(pos)

    def __hash__(slf):
        return slf.hash

    def __eq__(slf, otr):
        # Risky optimisation.
        return slf.hash == otr.hash

    def neighbors(slf, graph):
        for adj in graph.adjacencies[slf.pos]:
            yield Node(adj)

    def dist(slf, graph, otr):
        return 1


class RecNode:
    def __init__(slf, pos, level):
        slf.pos = pos
        slf.level = level
        slf.hash = hash((pos, level))

    def __hash__(slf):
        return slf.hash

    def __eq__(slf, otr):
        # Risky optimisation.
        return slf.hash == otr.hash

    def neighbors(slf, graph):
        for adj in graph.adjacencies[slf.pos]:
            if slf.pos in graph.teleports and adj in graph.teleports:
                if adj in graph.inner and slf.level > 0:
                    yield RecNode(adj, slf.level - 1)
                elif adj in graph.outer:
                    yield RecNode(adj, slf.level + 1)
            else:
                yield RecNode(adj, slf.level)

    def dist(slf, graph, otr):
        return 1 + abs(slf.level - otr.level)


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


def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from.keys():
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path


def astar(graph, starts, goal):
    # Initialise A* search.
    came_from = {}
    g_score = defaultdict(lambda: math.inf)
    f_score = defaultdict(lambda: math.inf)
    open = pqueue()
    for start in starts:
        g_score[start] = 0
        f_score[start] = start.dist(graph, goal)
        open.add(start, f_score[start])

    # Run A* search.
    while len(open) > 0:
        current = open.pop()
        if current == goal:
            return reconstruct_path(came_from, current)
        for neighbor in current.neighbors(graph):
            tentative = g_score[current] + 1
            if tentative < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative
                f_score[neighbor] = (
                    g_score[neighbor] + neighbor.dist(graph, goal)
                )
                open.add(neighbor, f_score[neighbor])


def aa_to_zz(maze):
    start = Node(maze.portals['AA'][0])
    end = Node(maze.portals['ZZ'][0])
    return len(astar(maze, [start], end)) - 1


def aa_to_zz_recursive(maze):
    start = RecNode(maze.portals['AA'][0], 0)
    end = RecNode(maze.portals['ZZ'][0], 0)
    return len(astar(maze, [start], end)) - 1


if __name__ == "__main__":
    solve(20, parse, aa_to_zz, aa_to_zz_recursive)
