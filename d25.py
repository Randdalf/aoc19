#!/usr/bin/env python

"""Advent of Code 2019, Day 25"""

from aoc19 import solve
from intcode import IntcodeCPU, OPCODE
from itertools import chain, combinations


def parse(data):
    return list(map(int, data.split(',')))


def drop_combinations(items):
    return map(
        frozenset,
        chain.from_iterable(
            combinations(items, r) for r in range(1, len(items) + 1)
        )
    )


def find_airlock_password(program):
    droid = IntcodeCPU(program)
    droid.execute()

    # Grant all safe items.
    items = {
        'jam': 4601,
        'loom': 4609,
        'mug': 4617,
        'spool of cat6': 4621,
        'prime number': 4625,
        'food ration': 4629,
        'fuel cell': 4645,
        'manifold': 4649
    }
    all_items = frozenset(items.keys())

    for addr in items.values():
        droid.memory[addr] = -1

    # Play the game!
    while droid.waiting_for_input:
        print(''.join(map(chr, droid.outputs)))
        droid.outputs.clear()
        command = input('')
        if command.startswith('#'):
            for dropped in drop_combinations(items):
                # Drop items we're not using.
                for item in dropped:
                    droid.inputs.extend(map(ord, f'drop {item}\n'))
                droid.execute()
                droid.outputs.clear()

                # Attempt to run the command.
                command = command.strip('#')
                droid.execute(*map(ord, command + '\n'))

                # Determine if we got past the security checkpoint.
                output = ''.join(map(chr, droid.outputs))
                if 'ejected' not in output:
                    words = output.split(' ')
                    return int(words[words.index('typing') + 1])

                # Pick up items we dropped.
                for item in dropped:
                    droid.inputs.extend(map(ord, f'take {item}\n'))
                droid.execute()
                droid.outputs.clear()
        else:
            droid.execute(*map(ord, command + '\n'))


if __name__ == "__main__":
    solve(25, parse, find_airlock_password)
