#!/usr/bin/env python3
import unittest
import os

os.sys.path.insert(0, os.getcwd())

from solutions import day12
from utility import inputs

class Part1(unittest.TestCase):
    def test_01(self):
        input = inputs.read("input12")
        result = day12.part1(input)
        self.assertEqual(result, 25)
    def test_in(self):
        input = inputs.read("input12_actual")
        result = day12.part1(input)
        self.assertEqual(result, 1032)

class Part2(unittest.TestCase):
    def test_01(self):
        input = inputs.read("input12")
        result = day12.part2(input)
        self.assertEqual(result, 286)
    def test_in(self):
        input = inputs.read("input12_actual")
        result = day12.part2(input)
        self.assertEqual(result, 156735)

if __name__ == '__main__':
    unittest.main(verbosity=2)