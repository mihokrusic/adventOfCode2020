#!/usr/bin/env python3
import unittest
import os

os.sys.path.insert(0, os.getcwd())

from solutions import day18
from utility import inputs

class Part1(unittest.TestCase):
    def test_01(self):
        input = inputs.read("input18")
        result = day18.part1(input)
        self.assertEqual(result, 26335)
    def test_in(self):
        input = inputs.read("input18_actual")
        result = day18.part1(input)
        self.assertEqual(result, 69490582260)

class Part2(unittest.TestCase):
    def test_01(self):
        input = inputs.read("input18")
        result = day18.part2(input)
        self.assertEqual(result, 693891)
    def test_in(self):
        input = inputs.read("input18_actual")
        result = day18.part2(input)
        self.assertEqual(result, 362464596624526)

if __name__ == '__main__':
    unittest.main(verbosity=2)