#!/usr/bin/env python

"""Advent of Code 2019, Day 5 (Unit Tests)"""

import unittest

from intcode import IntcodeComputer


example1 = [3,9,8,9,10,9,4,9,99,-1,8]
example2 = [3,9,7,9,10,9,4,9,99,-1,8]
example3 = [3,3,1108,-1,8,3,4,3,99]
example4 = [3,3,1107,-1,8,3,4,3,99]
example5 = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
example6 = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]
example6 = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]

class IntcodeTests(unittest.TestCase):
    def test_example1(slf):
        cpu = IntcodeComputer(example1)
        slf.assertEqual(cpu.execute(8)[-1], 1)
        slf.assertEqual(cpu.execute(13)[-1], 0)

    def test_example2(slf):
        cpu = IntcodeComputer(example2)
        slf.assertEqual(cpu.execute(7)[-1], 1)
        slf.assertEqual(cpu.execute(13)[-1], 0)

    def test_example3(slf):
        cpu = IntcodeComputer(example3)
        slf.assertEqual(cpu.execute(8)[-1], 1)
        slf.assertEqual(cpu.execute(13)[-1], 0)

    def test_example4(slf):
        cpu = IntcodeComputer(example4)
        slf.assertEqual(cpu.execute(7)[-1], 1)
        slf.assertEqual(cpu.execute(13)[-1], 0)

    def test_example5(slf):
        cpu = IntcodeComputer(example5)
        slf.assertEqual(cpu.execute(-1)[-1], 1)
        slf.assertEqual(cpu.execute(0)[-1], 0)
        slf.assertEqual(cpu.execute(1)[-1], 1)

    def test_example6(slf):
        cpu = IntcodeComputer(example6)
        slf.assertEqual(cpu.execute(7)[-1], 999)
        slf.assertEqual(cpu.execute(8)[-1], 1000)
        slf.assertEqual(cpu.execute(9)[-1], 1001)


if __name__ == "__main__":
    unittest.main()
