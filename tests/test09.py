#!/usr/bin/env python3
import unittest

from solutions import day09
from utility import inputs

class Part1(unittest.TestCase):
    def test_01(self):
        input = inputs.read("input09")
        result = day09.part1(input, 5)
        self.assertEqual(result, 127)
    def test_in(self):
        input = inputs.read("input09_actual")
        result = day09.part1(input, 25)
        self.assertEqual(result, 393911906)

class Part2(unittest.TestCase):
    def test_02(self):
        input = inputs.read("input09")
        result = day09.part2(input, 127)
        self.assertEqual(result, 62)
    def test_in(self):
        input = inputs.read("input09_actual")
        result = day09.part2(input, 393911906)
        self.assertEqual(result, 59341885)

if __name__ == '__main__':
    unittest.main(verbosity=2)