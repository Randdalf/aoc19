#!/usr/bin/env python

"""Advent of Code 2019, Day 6"""

from collections import defaultdict
import math
from pqueue import pqueue

from aoc19 import solve


def parse(data):
    orbits = defaultdict(list)
    for orbit in data.split('\n'):
        a, b = orbit.split(')')
        orbits[a].append(b)
    return orbits


def total_orbits(orbits, body, depth=0):
    return depth + sum(total_orbits(orbits, b, depth+1) for b in orbits[body])


def orbit_count_checksum(orbits, depth=0):
    return total_orbits(orbits, 'COM')


def orbital_transfers(orbits):
    # Build vertex graph.
    neighbors = defaultdict(list)
    graph = set()
    for a, bs in orbits.items():
        neighbors[a].extend(bs)
        for b in bs:
            neighbors[b].append(a)
        graph.add(a)
        graph.update(bs)
    source = 'YOU'
    target = 'SAN'

    # Dijkstra's algorithm.
    q = pqueue()
    dist = {v: math.inf for v in graph}
    prev = {v: None for v in graph}
    dist[source] = 0
    for v in graph:
        q.add(v, dist[v])

    while len(q):
        u = q.pop()
        for v in neighbors[u]:
            if v in q:
                alt = dist[u] + 1
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u
                    q.add(v, alt)

    # Shortest path.
    path = []
    u = target
    if prev[u] or u == source:
        while u:
            path.append(u)
            u = prev[u]

    return len(path) - 3


if __name__ == "__main__":
    solve(6, parse, orbit_count_checksum, orbital_transfers)
