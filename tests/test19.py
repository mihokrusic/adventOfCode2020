#!/usr/bin/env python3
import unittest
import os

os.sys.path.insert(0, os.getcwd())

from solutions import day19
from utility import inputs

class Part1(unittest.TestCase):
    def test_01(self):
        result = day19.solve(inputs.read_str("input19"), 1)
        self.assertEqual(result, 2)
    def test_02(self):
        result = day19.solve(inputs.read_str("input19_1"), 1)
        self.assertEqual(result, 3)
    def test_in(self):
        result = day19.solve(inputs.read_str("input19_actual"), 1)
        self.assertEqual(result, 149)

class Part2(unittest.TestCase):
    def test_01(self):
        result = day19.solve(inputs.read_str("input19_1"), 2)
        self.assertEqual(result, 12)
    def test_in(self):
        result = day19.solve(inputs.read_str("input19_actual"), 2)
        self.assertEqual(result, 332)

if __name__ == '__main__':
    unittest.main(verbosity=2)