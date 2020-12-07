#!/usr/bin/env python3
import unittest

from solutions import day07
from utility import inputs

class TestPart1(unittest.TestCase):
    def test_01(self):
        input = inputs.read("input07")
        result = day07.part1(input)
        self.assertEqual(result, 4)
    def test_in(self):
        input = inputs.read("input07_actual")
        result = day07.part1(input)
        self.assertEqual(result, 287)

class TestPart2(unittest.TestCase):
    def test_01(self):
        input = inputs.read("input07")
        result = day07.part2(input)
        self.assertEqual(result, 32)
    def test_02(self):
        input = inputs.read("input07_2")
        result = day07.part2(input)
        self.assertEqual(result, 126)
    def test_in(self):
        input = inputs.read("input07_actual")
        result = day07.part2(input)
        self.assertEqual(result, 48160)

if __name__ == '__main__':
    unittest.main(verbosity=2)