#!/usr/bin/env python

"""Advent of Code 2019, Day 15"""

from aoc19 import solve
from intcode import IntcodeCPU
from pathfind import astar
from pqueue import pqueue
from vec2 import manhattan, Vec2


class COMMAND:
    NORTH = 1
    SOUTH = 2
    WEST = 3
    EAST = 4


class STATUS:
    WALL = 0
    MOVED = 1
    OXYGEN = 2


dirs = {
    Vec2(0, -1): COMMAND.NORTH,
    Vec2(0, +1): COMMAND.SOUTH,
    Vec2(-1, 0): COMMAND.WEST,
    Vec2(+1, 0): COMMAND.EAST
}


def adjacencies(pos):
    for dir in dirs.keys():
        yield pos + dir


class Node:
    def __init__(slf, traversable, pos):
        slf.traversable = traversable
        slf.pos = pos

    def __hash__(slf):
        return hash(slf.pos)

    def __eq__(slf, otr):
        return slf.pos == otr.pos

    @property
    def neighbors(slf):
        for adj in adjacencies(slf.pos):
            if adj in slf.traversable:
                yield Node(slf.traversable, adj)

    def dist(slf, neighbor):
        return 1


def add_traversable(traversable, frontier, pos):
    traversable.add(pos)
    for adj in adjacencies(pos):
        if adj not in traversable:
            frontier.add(adj)


def find_path(traversable, src, dest):
    def goal(node):
        return node.pos == dest

    def h(node):
        return manhattan(node.pos, dest)

    return astar(Node(traversable, src), goal, h)


def map_area(program, stop_on_oxygen=False):
    droid = IntcodeCPU(program)
    pos = Vec2(0, 0)
    traversable = set()
    frontier = set()
    add_traversable(traversable, frontier, pos)

    while len(frontier) > 0:
        dest = frontier.pop()

        # Find the path from the current position to a frontier node using A*.
        traversable.add(dest)
        path = find_path(traversable, pos, dest)
        traversable.remove(dest)

        # Convert the path into a list of commands.
        commands = []
        for i in range(len(path) - 1):
            commands.append(dirs[path[i+1].pos - path[i].pos])

        # Execute the commands on the droid.
        droid.inputs.extend(reversed(commands))
        droid.execute()
        status = droid.outputs[-1]
        droid.outputs.clear()

        # Droid status informs our next action.
        if status == STATUS.WALL:
            pos = path[-2].pos
        else:
            add_traversable(traversable, frontier, dest)
            pos = dest

        if status == STATUS.OXYGEN:
            oxygen = dest
            if stop_on_oxygen:
                break

    return traversable, oxygen


def parse(data):
    return list(map(int, data.split(',')))


def fewest_commands_to_oxygen(program):
    traversable, oxygen = map_area(program, stop_on_oxygen=True)
    return len(find_path(traversable, Vec2(0, 0), oxygen)) - 1


def oxygen_saturation_mins(program):
    traversable, oxygen = map_area(program)
    oxygenated = {Node(traversable, oxygen)}
    mins = 0
    while len(oxygenated) < len(traversable):
        new = set()
        for node in oxygenated:
            new.update(node.neighbors)
        oxygenated.update(new)
        mins += 1
    return mins


if __name__ == "__main__":
    solve(15, parse, fewest_commands_to_oxygen, oxygen_saturation_mins)
