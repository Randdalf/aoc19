#!/usr/bin/env python

"""Advent of Code 2019, Day 23"""

from collections import deque

from aoc19 import solve
from intcode import IntcodeCPU


def parse(data):
    return list(map(int, data.split(',')))


def boot_network(program):
    # Initialise each CPU with its network address.
    cpus = [IntcodeCPU(program, addr) for addr in range(50)]
    queues = [deque() for cpu in cpus]

    # Run network until we see address 255.
    while True:
        for cpu, queue in zip(cpus, queues):
            if len(queue) > 0:
                while len(queue) > 0:
                    cpu.execute(*queue.popleft())
            else:
                cpu.execute(-1)
            for i in range(0, len(cpu.outputs), 3):
                addr, x, y = cpu.outputs[i:i+3]
                print(addr, x, y)
                if addr == 255:
                    return y
                queues[addr].append((x, y))
            cpu.outputs.clear()


if __name__ == "__main__":
    solve(23, parse, boot_network)
