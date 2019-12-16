#!/usr/bin/env python

"""Advent of Code 2019, Day 16 (Unit Tests)"""

import unittest

from d16 import parse, fft

example1 = "12345678"
example2 = "80871224585914546619083218645595"
example3 = "19617804207202209144916044189917"
example4 = "69317163492948606335995924319873"


class FFTTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(fft(parse(example1), 4), "01029498")

    def test_example2(slf):
        slf.assertEqual(fft(parse(example2), 100), "24176176")

    def test_example3(slf):
        slf.assertEqual(fft(parse(example3), 100), "73745418")

    def test_example4(slf):
        slf.assertEqual(fft(parse(example4), 100), "52432133")


if __name__ == "__main__":
    unittest.main()
