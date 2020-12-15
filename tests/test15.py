#!/usr/bin/env python3
import unittest
import os

os.sys.path.insert(0, os.getcwd())

from solutions import day15
from utility import inputs

class Part1(unittest.TestCase):
    def test_01(self):
        input = inputs.read("input15")
        result = day15.part1(input)
        self.assertEqual(result, 436)
    def test_02(self):
        input = inputs.read("input15_1")
        result = day15.part1(input)
        self.assertEqual(result, 1)
    def test_03(self):
        input = inputs.read("input15_2")
        result = day15.part1(input)
        self.assertEqual(result, 10)
    def test_04(self):
        input = inputs.read("input15_3")
        result = day15.part1(input)
        self.assertEqual(result, 27)
    def test_05(self):
        input = inputs.read("input15_4")
        result = day15.part1(input)
        self.assertEqual(result, 78)
    def test_06(self):
        input = inputs.read("input15_5")
        result = day15.part1(input)
        self.assertEqual(result, 438)
    def test_07(self):
        input = inputs.read("input15_6")
        result = day15.part1(input)
        self.assertEqual(result, 1836)
    def test_in(self):
        input = inputs.read("input15_actual")
        result = day15.part1(input)
        self.assertEqual(result, 211)

class Part2(unittest.TestCase):
    def test_in(self):
        input = inputs.read("input15_actual")
        result = day15.part2(input)
        self.assertEqual(result, 2159626)

if __name__ == '__main__':
    unittest.main(verbosity=2)