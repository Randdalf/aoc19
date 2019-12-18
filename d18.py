#!/usr/bin/env python

"""Advent of Code 2019, Day 18"""

from collections import defaultdict
import math

from aoc19 import solve
from pqueue import pqueue
from vec2 import Vec2


class Vault:
    def __init__(slf, entrance, passages):
        slf.entrance = entrance
        slf.passages = passages
        slf.keys = {key: pos for pos, key in passages.items() if key.islower()}


class Node:
    def __init__(slf, pos, keys):
        slf.pos = pos
        slf.keys = keys

    def __hash__(slf):
        return hash(('Node', slf.pos, slf.keys))

    def __eq__(slf, otr):
        return slf.pos == otr.pos and slf.keys == otr.keys

    def __str__(slf):
        return f'Node({slf.pos}, {slf.keys})'


dirs = [
    Vec2(0, -1),
    Vec2(1, 0),
    Vec2(0, 1),
    Vec2(-1, 0)
]


def parse(data):
    passages = {}
    for y, row in enumerate(data.split('\n')):
        for x, tile in enumerate(row):
            pos = Vec2(x, y)
            if tile != '#':
                passages[pos] = tile
            if tile == '@':
                entrance = pos
    return Vault(entrance, passages)


def neighbors(node, vault):
    for dir in dirs:
        adj = node.pos + dir
        if adj in vault.passages:
            tile = vault.passages[adj]
            if tile.islower():
                yield Node(adj, node.keys | {tile})
            elif tile.isupper():
                if tile.lower() in node.keys:
                    yield Node(adj, node.keys)
            else:
                yield Node(adj, node.keys)


def manhattan(a, b):
    return abs(a.x - b.x) + abs(a.y - b.y)


def dist(vault, a, b):
    delta = len(b.keys) - len(a.keys)
    if delta < 0:
        return math.inf
    else:
        return manhattan(a.pos, b.pos)


def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from.keys():
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path


def astar(vault, start, goal):
    # Initialise A* search.
    came_from = {}
    g_score = defaultdict(lambda: math.inf)
    g_score[start] = 0
    f_score = defaultdict(lambda: math.inf)
    f_score[start] = dist(vault, start, goal)
    open = pqueue()
    open.add(start, f_score[start])

    # Run A* search.
    while len(open) > 0:
        current = open.pop()
        if len(current.keys) == len(goal.keys):
            return reconstruct_path(came_from, current)
        for neighbor in neighbors(current, vault):
            tentative = g_score[current] + 1
            if tentative < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative
                f_score[neighbor] = (
                    g_score[neighbor] + dist(vault, neighbor, goal)
                )
                if neighbor in open:
                    open.remove(neighbor)
                open.add(neighbor, f_score[neighbor])


def shortest_path(vault):
    start = Node(vault.entrance, frozenset())
    shortest = None
    goal = Node(start.pos, frozenset(vault.keys.keys()))
    path = astar(vault, start, goal)
    return len(path) - 1


if __name__ == "__main__":
    solve(18, parse, shortest_path)
