#!/usr/bin/env python

"""Advent of Code 2019, Day 22"""

from aoc19 import solve


class TECHNIQUE:
    CUT = 'cut'
    DEAL = 'deal with increment'
    NEW = 'deal into new stack'


def parse(data):
    commands = []
    for line in data.split('\n'):
        if line == TECHNIQUE.NEW:
            commands.append((TECHNIQUE.NEW,))
        elif line.startswith(TECHNIQUE.CUT):
            cut = int(line.replace(TECHNIQUE.CUT, '').strip())
            commands.append((TECHNIQUE.CUT, cut))
        elif line.startswith(TECHNIQUE.DEAL):
            step = int(line.replace(TECHNIQUE.DEAL, '').strip())
            commands.append((TECHNIQUE.DEAL, step))
    return commands


def shuffle(commands, n=10007):
    deck = list(range(n))
    for command in commands:
        if command[0] == TECHNIQUE.NEW:
            deck.reverse()
        elif command[0] == TECHNIQUE.CUT:
            cut = command[1]
            deck = deck[cut:] + deck[:cut]
        elif command[0] == TECHNIQUE.DEAL:
            step = command[1]
            dealt = list(deck)
            for i, card in enumerate(deck):
                dealt[(i * step) % n] = card
            deck = dealt
    return deck


def shuffle_2019(commands):
    return shuffle(commands).index(2019)


if __name__ == "__main__":
    solve(22, parse, shuffle_2019)
