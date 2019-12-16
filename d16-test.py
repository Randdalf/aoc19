#!/usr/bin/env python

"""Advent of Code 2019, Day 16 (Unit Tests)"""

import unittest

from d16 import parse, fft, real_signal

example1 = "12345678"
example2 = "80871224585914546619083218645595"
example3 = "19617804207202209144916044189917"
example4 = "69317163492948606335995924319873"
example5 = "03036732577212944063491565474664"
example6 = "02935109699940807407585447034323"
example7 = "03081770884921959731165446850517"


class FFTTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(fft(parse(example1), 4), "01029498")

    def test_example2(slf):
        slf.assertEqual(fft(parse(example2)), "24176176")

    def test_example3(slf):
        slf.assertEqual(fft(parse(example3)), "73745418")

    def test_example4(slf):
        slf.assertEqual(fft(parse(example4)), "52432133")


class RealSignalTests(unittest.TestCase):
    def test_example5(slf):
        slf.assertEqual(real_signal(parse(example5)), "84462026")

    def test_example6(slf):
        slf.assertEqual(real_signal(parse(example6)), "78725270")

    def test_example7(slf):
        slf.assertEqual(real_signal(parse(example7)), "53553731")


if __name__ == "__main__":
    unittest.main()
