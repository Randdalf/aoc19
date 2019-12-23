#!/usr/bin/env python

"""Advent of Code 2019, Day 23"""

from collections import deque

from aoc19 import solve
from intcode import IntcodeCPU


def parse(data):
    return list(map(int, data.split(',')))


def initialize_cpus(program):
    cpus = [IntcodeCPU(program, addr) for addr in range(50)]
    queues = [deque() for cpu in cpus]
    return cpus, queues


def run_until_255(program):
    cpus, queues = initialize_cpus(program)

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
                if addr == 255:
                    return y
                queues[addr].append((x, y))
            cpu.outputs.clear()


def nat_repeat(program):
    cpus, queues = initialize_cpus(program)

    # Run network until we see a repeated NAT value.
    seen = set()
    nat = (None, None)
    while True:
        idle = True
        for cpu, queue in zip(cpus, queues):
            if len(queue) > 0:
                while len(queue) > 0:
                    cpu.execute(*queue.popleft())
                idle = False
            else:
                cpu.execute(-1)
            for i in range(0, len(cpu.outputs), 3):
                addr, x, y = cpu.outputs[i:i+3]
                if addr == 255:
                    nat = (x, y)
                else:
                    queues[addr].append((x, y))
                idle = False
            cpu.outputs.clear()
        if idle:
            if nat[1] in seen:
                return nat[1]
            else:
                seen.add(nat[1])
            queues[0].append(nat)


if __name__ == "__main__":
    solve(23, parse, run_until_255, nat_repeat)
