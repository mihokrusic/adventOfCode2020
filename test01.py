#!/usr/bin/env python3
import unittest

from solutions import day01
from utility import inputs

class TestDay01Part1(unittest.TestCase):
    def test01(self):
        result = day01.part1('')
        self.assertEqual(result, 1)

class TestDay01Part2(unittest.TestCase):
    def test01(self):
        result = day01.part2('')
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main(verbosity=2)