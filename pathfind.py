#!/usr/bin/env python

"""Advent of Code 2019, Path Finding Algorithms"""

from collections import defaultdict, deque
import math

from pqueue import pqueue


def reconstruct_path(prev, node):
    """Return the nodes on the path from the given node to the source node."""
    if node in prev.keys():
        path = [node]
        while node in prev.keys():
            node = prev[node]
            path.append(node)
        path.reverse()
        return path


def path_length(path):
    """Returns the length of path connecting the given list of nodes."""
    return sum(path[i].dist(path[i+1]) for i in range(len(path) - 1))


def bfs(src):
    """Breadth-First Search.

    Returns the closest distance to every other node from the source node, and
    each previous node on the path from the source node to every other node.
    """
    q = deque()
    dist = defaultdict(lambda: math.inf)
    prev = {}

    dist[src] = 0
    q.append(src)

    while len(q) > 0:
        current = q.popleft()
        for neighbor in current.neighbors:
            alt = dist[current] + current.dist(neighbor)
            if alt < dist[neighbor]:
                dist[neighbor] = alt
                prev[neighbor] = current
                q.append(neighbor)
    return dist, prev


def dijkstra(src, goal):
    """Dijkstra's algorithm.

    Returns a path from the given source node to the node which satsifies the
    given goal predicate.
    """
    q = pqueue()
    dist = defaultdict(lambda: math.inf)
    prev = {}

    dist[src] = 0
    q.add(src, dist[src])

    while len(q) > 0:
        current = q.pop()
        if goal(current):
            return reconstruct_path(prev, current)
        for neighbor in current.neighbors:
            alt = dist[current] + current.dist(neighbor)
            if alt < dist[neighbor]:
                dist[neighbor] = alt
                prev[neighbor] = current
                q.add(neighbor, alt)


def astar(src, goal, h):
    """A* search algorithm.

    Returns a path from the given source node to the node which satsifies the
    given goal predicate. Accepts a heuristic function which estimates the cost
    of reaching the goal node, which guides the search to a faster result.
    """
    q = pqueue()
    g = defaultdict(lambda: math.inf)
    f = defaultdict(lambda: math.inf)
    prev = {}

    g[src] = 0
    f[src] = h(src)
    q.add(src, f[src])

    while len(q) > 0:
        current = q.pop()
        if goal(current):
            return reconstruct_path(prev, current)
        for neighbor in current.neighbors:
            alt = g[current] + current.dist(neighbor)
            if alt < g[neighbor]:
                prev[neighbor] = current
                g[neighbor] = alt
                f[neighbor] = g[neighbor] + h(neighbor)
                q.add(neighbor, f[neighbor])
