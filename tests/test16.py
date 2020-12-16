#!/usr/bin/env python3
import unittest
import os

os.sys.path.insert(0, os.getcwd())

from solutions import day16
from utility import inputs

class Part1(unittest.TestCase):
    def test_01(self):
        input = inputs.read("input16")
        result = day16.part1(input)
        self.assertEqual(result, 71)
    def test_in(self):
        input = inputs.read("input16_actual")
        result = day16.part1(input)
        self.assertEqual(result, 22073)

class Part2(unittest.TestCase):
    def test_in(self):
        input = inputs.read("input16_actual")
        result = day16.part2(input)
        self.assertEqual(result, 1346570764607)

if __name__ == '__main__':
    unittest.main(verbosity=2)