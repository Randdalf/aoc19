#!/usr/bin/env python

"""Advent of Code 2019, Priority Queue"""

from itertools import count
from heapq import heappush
from heapq import heappop


class pqueue:
    def __init__(slf):
        slf.pq = []
        slf.finder = {}
        slf.counter = count()
        slf.n = 0

    def add(slf, task, priority):
        if task in slf.finder:
            slf.remove(task)
        entry = [priority, next(slf.counter), task]
        slf.finder[task] = entry
        heappush(slf.pq, entry)
        slf.n += 1

    def remove(slf, task):
        entry = slf.finder.pop(task)
        entry[-1] = None
        slf.n -= 1

    def pop(slf):
        while slf.pq:
            priority, count, task = heappop(slf.pq)
            if task:
                slf.remove(task)
                return task

    def __len__(slf):
        return slf.n

    def __contains__(slf, task):
        return task in slf.finder
