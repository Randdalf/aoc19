#!/usr/bin/env python

"""Advent of Code 2019, Day 9 (Unit Tests)"""

import unittest

from intcode import intcode


class IntcodeTests(unittest.TestCase):
    def test_example1(slf):
        example1 = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
        outputs = intcode(example1).outputs
        slf.assertEqual(example1, outputs)

    def test_example2(slf):
        example2 = [1102,34915192,34915192,7,4,7,99,0]
        output = intcode(example2).outputs[0]
        slf.assertEqual(len(str(output)), 16)

    def test_example3(slf):
        example3 = [104,1125899906842624,99]
        output = intcode(example3).outputs[0]
        slf.assertEqual(1125899906842624, output)

if __name__ == "__main__":
    unittest.main()
