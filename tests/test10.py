#!/usr/bin/env python3
import unittest
import os

os.sys.path.insert(0, os.getcwd())

from solutions import day10
from utility import inputs

class Part1(unittest.TestCase):
    def test_01(self):
        input = inputs.read("input10_1")
        result = day10.part1(input)
        self.assertEqual(result, 35)
    def test_02(self):
        input = inputs.read("input10_2")
        result = day10.part1(input)
        self.assertEqual(result, 220)
    def test_in(self):
        input = inputs.read("input10_actual")
        result = day10.part1(input)
        self.assertEqual(result, 2170)

class Part2(unittest.TestCase):
    def test_01(self):
        input = inputs.read("input10_1")
        result = day10.part2(input)
        self.assertEqual(result, 8)
    def test_02(self):
        input = inputs.read("input10_2")
        result = day10.part2(input)
        self.assertEqual(result, 19208)
    def test_in(self):
        input = inputs.read("input10_actual")
        result = day10.part2(input)
        self.assertEqual(result, 24803586664192)

if __name__ == '__main__':
    unittest.main(verbosity=2)