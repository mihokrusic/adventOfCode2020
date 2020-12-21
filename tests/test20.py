#!/usr/bin/env python3
import unittest
import os

os.sys.path.insert(0, os.getcwd())

from solutions import day20
from utility import inputs

class Part1(unittest.TestCase):
    def test_01(self):
        result = day20.solve(inputs.read_str("input20"), 1)
        self.assertEqual(result, 20899048083289)
    def test_in(self):
        result = day20.solve(inputs.read_str("input20_actual"), 1)
        self.assertEqual(result, 63187742854073)

class Part2(unittest.TestCase):
    def test_01(self):
        result = day20.solve(inputs.read_str("input20"), 2)
        self.assertEqual(result, 273)
    # def test_in(self):
    #     result = day20.solve(inputs.read_str("input20_actual"), 2)
    #     self.assertEqual(result, 2152)

if __name__ == '__main__':
    unittest.main(verbosity=2)