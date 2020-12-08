#!/usr/bin/env python3
import unittest

from solutions import day10
from utility import inputs

class Part1(unittest.TestCase):
    def test_01(self):
        input = inputs.read("input10")
        result = day10.part1(input)
        self.assertEqual(result, 1)
    def test_in(self):
        input = inputs.read("input10_actual")
        result = day10.part1(input)
        self.assertEqual(result, 1)

class Part2(unittest.TestCase):
    def test_02(self):
        input = inputs.read("input10")
        result = day10.part2(input)
        self.assertEqual(result, 2)
    def test_in(self):
        input = inputs.read("input10_actual")
        result = day10.part2(input)
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main(verbosity=2)