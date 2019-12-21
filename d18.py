#!/usr/bin/env python

"""Advent of Code 2019, Day 18"""

from itertools import chain

from aoc19 import solve
from pathfind import bfs, dijkstra, path_length, reconstruct_path
from vec2 import Vec2

dirs = [
    Vec2(0, -1),
    Vec2(1, 0),
    Vec2(0, 1),
    Vec2(-1, 0)
]


class Vault:
    def __init__(slf, entrance, passages):
        slf.entrance = entrance
        slf.passages = passages
        slf.keys = {key: pos for pos, key in passages.items() if key.islower()}


class PassageNode:
    def __init__(slf, vault, pos):
        slf.vault = vault
        slf.pos = pos
        slf.tile = vault.passages[slf.pos]

    def __hash__(slf):
        return hash(slf.pos)

    def __eq__(slf, otr):
        return slf.pos == otr.pos

    @property
    def neighbors(slf):
        for dir in dirs:
            adj = slf.pos + dir
            if adj in slf.vault.passages:
                yield PassageNode(slf.vault, adj)

    def dist(slf, neighbor):
        return 1

    def __str__(slf):
        return f'PassageNode({slf.pos.x}, {slf.pos.y}, {slf.tile})'


class KeyNode:
    def __init__(slf, cache, key, collected):
        slf.cache = cache
        slf.key = key
        slf.collected = collected

    def __hash__(slf):
        return hash((slf.key, slf.collected))

    def __eq__(slf, otr):
        return slf.key == otr.key and slf.collected == otr.collected

    @property
    def neighbors(slf):
        for dest, (dist, required) in slf.cache[slf.key].items():
            if dest not in slf.collected and required <= slf.collected:
                yield KeyNode(slf.cache, dest, slf.collected | frozenset(dest))

    def dist(slf, neighbor):
        return slf.cache[slf.key][neighbor.key][0]

    def __str__(slf):
        return f'KeyNode({slf.key}, {set(slf.collected)})'


class QuadKeyNode:
    def __init__(slf, cache, active, keys, collected):
        slf.cache = cache
        slf.active = active
        slf.keys = keys
        slf.collected = collected

    def __hash__(slf):
        return hash((slf.keys, slf.collected))

    def __eq__(slf, otr):
        return (
            slf.keys == otr.keys and
            slf.collected == otr.collected and
            slf.active == otr.active
        )

    @property
    def neighbors(slf):
        i = slf.active
        for dest, (dist, required) in slf.cache[slf.keys[i]].items():
            if dest not in slf.collected and required <= slf.collected:
                keys = slf.keys[:i] + (dest,) + slf.keys[i+1:]
                collected = slf.collected | frozenset(dest)
                yield QuadKeyNode(slf.cache, i, keys, collected)
        j = (i + 1) % len(slf.keys)
        yield QuadKeyNode(slf.cache, j, slf.keys, slf.collected)

    def dist(slf, neighbor):
        dist = 0
        for src, dest in zip(slf.keys, neighbor.keys):
            paths = slf.cache[src]
            if dest in paths:
                dist += paths[dest][0]
        return dist

    def __str__(slf):
        return f'QuadKeyNode({slf.keys}, {set(slf.collected)})'


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


def compute_path_cache(vault, entrances):
    # Find the distance from each key and entrance to every other key, and
    # the keys required to take that path.
    cache = {}
    for src, pos in chain(vault.keys.items(), entrances):
        dists, prev = bfs(PassageNode(vault, pos))
        cache[src] = {}
        for dest, pos in vault.keys.items():
            if src != dest:
                path = reconstruct_path(prev, PassageNode(vault, pos))
                if path:
                    collected = set()
                    required = set()
                    for tile in [vault.passages[node.pos] for node in path]:
                        if tile.isupper() and tile.lower() not in collected:
                            required.add(tile.lower())
                        elif tile.islower():
                            collected.add(tile)
                    cache[src][dest] = (len(path) - 1, frozenset(required))
    return cache


def shortest_path(vault):
    def goal(node):
        return len(node.collected) == len(vault.keys)

    cache = compute_path_cache(vault, [('@', vault.entrance)])
    path = dijkstra(KeyNode(cache, '@', frozenset()), goal)
    return path_length(path)


def quad_droid(vault):
    def goal(node):
        return len(node.collected) == len(vault.keys)

    del vault.passages[vault.entrance]
    for dir in dirs:
        del vault.passages[vault.entrance + dir]
    entrances = [
        ('1', vault.entrance + Vec2(-1, -1)),
        ('2', vault.entrance + Vec2(+1, -1)),
        ('3', vault.entrance + Vec2(+1, +1)),
        ('4', vault.entrance + Vec2(-1, +1)),
    ]
    cache = compute_path_cache(vault, entrances)
    src = QuadKeyNode(cache, 0, ('1', '2', '3', '4'), frozenset())
    path = dijkstra(src, goal)
    return path_length(path)


if __name__ == "__main__":
    solve(18, parse, shortest_path, quad_droid)
