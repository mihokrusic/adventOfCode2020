#!/usr/bin/env python3
import unittest

from solutions import day02
from utility import inputs

class Part1(unittest.TestCase):
    def test_01(self):
        input = inputs.read("input02")
        result = day02.part1(input)
        self.assertEqual(result, 2)

    def test_in(self):
        input = inputs.read("input02_actual")
        result = day02.part1(input)
        self.assertEqual(result, 528)

class Part2(unittest.TestCase):
    def test_01(self):
        input = inputs.read("input02")
        result = day02.part2(input)
        self.assertEqual(result, 1)

    def test_in(self):
        input = inputs.read("input02_actual")
        result = day02.part2(input)
        self.assertEqual(result, 497)

if __name__ == '__main__':
    unittest.main(verbosity=2)