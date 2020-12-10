#!/usr/bin/env python3
import unittest
import os

os.sys.path.insert(0, os.getcwd())

from solutions import day06
from utility import inputs

class Part1(unittest.TestCase):
    def test_01(self):
        input = inputs.read("input06")
        result = day06.part1(input)
        self.assertEqual(result, 11)
    def test_in(self):
        input = inputs.read("input06_actual")
        result = day06.part1(input)
        self.assertEqual(result, 6583)

class Part2(unittest.TestCase):
    def test_01(self):
        input = inputs.read("input06")
        result = day06.part2(input)
        self.assertEqual(result, 6)
    def test_in(self):
        input = inputs.read("input06_actual")
        result = day06.part2(input)
        self.assertEqual(result, 3290)

if __name__ == '__main__':
    unittest.main(verbosity=2)