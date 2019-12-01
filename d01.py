#!/usr/bin/env pytho

"""Advent of Code 2019, Day 1"""

import math

from aoc19 import solve


def parse(data):
    return list(map(int, data.split('\n')))


def fuel_requirement(mass):
    return (mass // 3) - 2


def sum_fuel_requirements(masses):
    return sum(fuel_requirement(mass) for mass in masses)


def true_fuel_requirement(mass):
    fuel = fuel_requirement(mass)
    return 0 if fuel < 0 else fuel + true_fuel_requirement(fuel)


def sum_true_fuel_requirements(masses):
    return sum(true_fuel_requirement(mass) for mass in masses)


if __name__ == "__main__":
    solve(1, parse, sum_fuel_requirements, sum_true_fuel_requirements)
