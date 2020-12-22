#!/usr/bin/env python3
import unittest
import os

os.sys.path.insert(0, os.getcwd())

from solutions import day22
from utility import inputs

class Part1(unittest.TestCase):
    def test_01(self):
        result = day22.solve(inputs.read_str("input22"), 1)
        self.assertEqual(result, 306)
    def test_in(self):
        result = day22.solve(inputs.read_str("input22_actual"), 1)
        self.assertEqual(result, 32272)

class Part2(unittest.TestCase):
    def test_01(self):
        result = day22.solve(inputs.read_str("input22"), 2)
        self.assertEqual(result, 291)
    def test_in(self):
        result = day22.solve(inputs.read_str("input22_actual"), 2)
        self.assertEqual(result, 33206)

if __name__ == '__main__':
    unittest.main(verbosity=2)