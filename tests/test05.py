#!/usr/bin/env python3
import unittest

from solutions import day05
from utility import inputs

class Part1(unittest.TestCase):
    def test_01(self):
        result = day05.get_seat_id('BFFFBBFRRR')
        self.assertEqual(result, 567)
    def test_02(self):
        result = day05.get_seat_id('FFFBBBFRRR')
        self.assertEqual(result, 119)
    def test_03(self):
        result = day05.get_seat_id('BBFFBBFRLL')
        self.assertEqual(result, 820)
    def test_in(self):
        input = inputs.read("input05_actual")
        result = day05.part1(input)
        self.assertEqual(result, 890)

class Part2(unittest.TestCase):
    def test_in(self):
        input = inputs.read("input05_actual")
        result = day05.part2(input)
        self.assertEqual(result, 651)

if __name__ == '__main__':
    unittest.main(verbosity=2)