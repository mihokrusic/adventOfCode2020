#!/usr/bin/env python3
import unittest
import os

os.sys.path.insert(0, os.getcwd())

from solutions import day14
from utility import inputs

class Part1(unittest.TestCase):
    def test_01(self):
        input = inputs.read("input14")
        result = day14.part1(input)
        self.assertEqual(result, 165)
    def test_in(self):
        input = inputs.read("input14_actual")
        result = day14.part1(input)
        self.assertEqual(result, 14954914379452)

class Part2(unittest.TestCase):
    def test_01(self):
        input = inputs.read("input14_2")
        result = day14.part2(input)
        self.assertEqual(result, 208)
    def test_in(self):
        input = inputs.read("input14_actual")
        result = day14.part2(input)
        self.assertEqual(result, 3415488160714)

if __name__ == '__main__':
    unittest.main(verbosity=2)