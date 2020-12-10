#!/usr/bin/env python3
import unittest
import os

os.sys.path.insert(0, os.getcwd())

from solutions import day04
from utility import inputs

class Part1(unittest.TestCase):
    def test_01(self):
        input = inputs.read("input04")
        result = day04.part1(input)
        self.assertEqual(result, 2)
    def test_in(self):
        input = inputs.read("input04_actual")
        result = day04.part1(input)
        self.assertEqual(result, 208)

class Part2(unittest.TestCase):
    def test_01(self):
        input = inputs.read("input04_2_1")
        result = day04.part2(input)
        self.assertEqual(result, 0)
    def test_02(self):
        input = inputs.read("input04_2_2")
        result = day04.part2(input)
        self.assertEqual(result, 4)
    def test_in(self):
        input = inputs.read("input04_actual")
        result = day04.part2(input)
        self.assertEqual(result, 167)

if __name__ == '__main__':
    unittest.main(verbosity=2)