#!/usr/bin/env python3
import unittest
import os

os.sys.path.insert(0, os.getcwd())

from solutions import day13
from utility import inputs

class Part1(unittest.TestCase):
    def test_01(self):
        input = inputs.read("input13")
        result = day13.part1(input)
        self.assertEqual(result, 295)
    def test_in(self):
        input = inputs.read("input13_actual")
        result = day13.part1(input)
        self.assertEqual(result, 4207)

class Part2(unittest.TestCase):
    def test_01(self):
        input = inputs.read("input13")
        result = day13.part2(input)
        self.assertEqual(result, 1068781)
    def test_02(self):
        input = inputs.read("input13_2_1")
        result = day13.part2(input)
        self.assertEqual(result, 3417)
    def test_03(self):
        input = inputs.read("input13_2_2")
        result = day13.part2(input)
        self.assertEqual(result, 754018)
    def test_04(self):
        input = inputs.read("input13_2_3")
        result = day13.part2(input)
        self.assertEqual(result, 779210)
    def test_05(self):
        input = inputs.read("input13_2_4")
        result = day13.part2(input)
        self.assertEqual(result, 1261476)
    def test_06(self):
        input = inputs.read("input13_2_5")
        result = day13.part2(input)
        self.assertEqual(result, 1202161486)
    def test_in(self):
        input = inputs.read("input13_actual")
        result = day13.part2(input)
        self.assertEqual(result, 725850285300475)

if __name__ == '__main__':
    unittest.main(verbosity=2)