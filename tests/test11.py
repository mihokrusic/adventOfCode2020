#!/usr/bin/env python3
import unittest
import os

os.sys.path.insert(0, os.getcwd())

from solutions import day11
from utility import inputs

class Part1(unittest.TestCase):
    def test_01(self):
        input = inputs.read("input11")
        result = day11.part1(input)
        self.assertEqual(result, 1)
    # def test_in(self):
    #     input = inputs.read("input11_actual")
    #     result = day11.part1(input)
    #     self.assertEqual(result, 1)

class Part2(unittest.TestCase):
    def test_01(self):
        input = inputs.read("input11")
        result = day11.part2(input)
        self.assertEqual(result, 2)
    # def test_in(self):
    #     input = inputs.read("input11_actual")
    #     result = day11.part2(input)
    #     self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main(verbosity=2)