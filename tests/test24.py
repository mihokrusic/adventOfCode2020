#!/usr/bin/env python3
import unittest
import os

os.sys.path.insert(0, os.getcwd())

from solutions import day24
from utility import inputs

class Part1(unittest.TestCase):
    def test_01(self):
        result = day24.solve(inputs.read_str("input24"), 1)
        self.assertEqual(result, 10)
    def test_in(self):
        result = day24.solve(inputs.read_str("input24_actual"), 1)
        self.assertEqual(result, 436)

class Part2(unittest.TestCase):
    def test_01(self):
        result = day24.solve(inputs.read_str("input24"), 2)
        self.assertEqual(result, 2208)
    # def test_in(self):
    #     result = day24.solve(inputs.read_str("input24_actual"), 2)
    #     self.assertEqual(result, 4133)

if __name__ == '__main__':
    unittest.main(verbosity=2)