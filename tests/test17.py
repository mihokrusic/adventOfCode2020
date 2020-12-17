#!/usr/bin/env python3
import unittest
import os

os.sys.path.insert(0, os.getcwd())

from solutions import day17
from utility import inputs

class Part1(unittest.TestCase):
    def test_01(self):
        input = inputs.read("input17")
        result = day17.part1(input)
        self.assertEqual(result, 112)
    def test_in(self):
        input = inputs.read("input17_actual")
        result = day17.part1(input)
        self.assertEqual(result, 322)

class Part2(unittest.TestCase):
    def test_01(self):
        input = inputs.read("input17")
        result = day17.part2(input)
        self.assertEqual(result, 848)
    def test_in(self):
        input = inputs.read("input17_actual")
        result = day17.part2(input)
        self.assertEqual(result, 2000)

if __name__ == '__main__':
    unittest.main(verbosity=2)