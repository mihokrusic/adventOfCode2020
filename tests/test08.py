#!/usr/bin/env python3
import unittest
import os

os.sys.path.insert(0, os.getcwd())

from solutions import day08
from utility import inputs

class Part1(unittest.TestCase):
    def test_01(self):
        input = inputs.read("input08")
        result = day08.part1(input)
        self.assertEqual(result, 5)
    def test_in(self):
        input = inputs.read("input08_actual")
        result = day08.part1(input)
        self.assertEqual(result, 1949)

class Part2(unittest.TestCase):
    def test_02(self):
        input = inputs.read("input08")
        result = day08.part2(input)
        self.assertEqual(result, 8)
    def test_in(self):
        input = inputs.read("input08_actual")
        result = day08.part2(input)
        self.assertEqual(result, 2092)

if __name__ == '__main__':
    unittest.main(verbosity=2)