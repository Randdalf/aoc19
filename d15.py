#!/usr/bin/env python

"""Advent of Code 2019, Day 15"""

from collections import defaultdict
import math

from aoc19 import solve
from intcode import IntcodeCPU
from pqueue import pqueue
from vec2 import Vec2


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


def manhattan(a, b):
    return abs(a.x - b.x) + abs(a.y - b.y)


def parse(data):
    return list(map(int, data.split(',')))


def adjacencies(node):
    for dir in dirs.keys():
        yield node + dir


def neighbors(node, nodes):
    for adj in adjacencies(node):
        if adj in nodes:
            yield adj


def add_node(nodes, frontier, node):
    nodes.add(node)
    for adj in adjacencies(node):
        if adj not in nodes:
            frontier.add(adj)


def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from.keys():
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path


def astar(nodes, start, goal, h):
    came_from = {}
    g_score = defaultdict(lambda: math.inf)
    g_score[start] = 0
    f_score = defaultdict(lambda: math.inf)
    f_score[start] = h(start, goal)
    open = pqueue()
    open.add(start, f_score[start])
    while len(open) > 0:
        current = open.pop()
        if current == goal:
            return reconstruct_path(came_from, current)
        for neighbor in neighbors(current, nodes):
            tentative = g_score[current] + 1
            if tentative < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative
                f_score[neighbor] = g_score[neighbor] + h(neighbor, goal)
                if neighbor in open:
                    open.remove(neighbor)
                open.add(neighbor, f_score[neighbor])


def map_area(program, stop_on_oxygen=False):
    droid = IntcodeCPU(program)
    pos = Vec2(0, 0)
    nodes = set()
    frontier = set()
    add_node(nodes, frontier, pos)

    while len(frontier) > 0:
        goal = frontier.pop()

        # Find the path from the current position to a frontier node using A*.
        nodes.add(goal)
        path = astar(nodes, pos, goal, manhattan)
        nodes.remove(goal)

        # Convert the path into a list of commands.
        commands = []
        for i in range(len(path) - 1):
            commands.append(dirs[path[i+1] - path[i]])

        # Execute the commands on the droid.
        droid.inputs.extend(reversed(commands))
        droid.execute()
        status = droid.outputs[-1]
        droid.outputs.clear()

        # Droid status informs our next action.
        if status == STATUS.WALL:
            pos = path[-2]
        else:
            add_node(nodes, frontier, goal)
            pos = goal

        if status == STATUS.OXYGEN:
            oxygen = goal
            if stop_on_oxygen:
                break

    return nodes, oxygen


def fewest_commands_to_oxygen(program):
    nodes, oxygen = map_area(program, stop_on_oxygen=True)
    return len(astar(nodes, Vec2(0, 0), oxygen, manhattan)) - 1


def oxygen_saturation_mins(program):
    nodes, oxygen = map_area(program)
    oxygenated = {oxygen}
    mins = 0
    while len(oxygenated) < len(nodes):
        new = set()
        for node in oxygenated:
            new.update(neighbors(node, nodes))
        oxygenated.update(new)
        mins += 1
    return mins


if __name__ == "__main__":
    solve(15, parse, fewest_commands_to_oxygen, oxygen_saturation_mins)
