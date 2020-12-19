#!/usr/bin/env python3
import unittest
import os

os.sys.path.insert(0, os.getcwd())

from solutions import day19
from utility import inputs

class Part1(unittest.TestCase):
    def test_01(self):
        input = inputs.read("input19")
        result = day19.part1(input)
        self.assertEqual(result, 2)
    def test_02(self):
        input = inputs.read("input19_1")
        result = day19.part1(input)
        self.assertEqual(result, 3)
    def test_in(self):
        input = inputs.read("input19_actual")
        result = day19.part1(input)
        self.assertEqual(result, 149)

# class Part2(unittest.TestCase):
#     def test_01(self):
#         input = inputs.read("input19_1")
#         result = day19.part2(input)
#         self.assertEqual(result, 3)
#     def test_in(self):
#         input = inputs.read("input19_actual")
#         result = day19.part2(input)
#         self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main(verbosity=2)