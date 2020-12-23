#!/usr/bin/env python3
import unittest
import os

os.sys.path.insert(0, os.getcwd())

from solutions import day23

class Part1(unittest.TestCase):
    def test_01(self):
        result = day23.solve('389125467', 1)
        self.assertEqual(result, '67384529')
    def test_in(self):
        result = day23.solve('916438275', 1)
        self.assertEqual(result, '39564287')

class Part2(unittest.TestCase):
    def test_01(self):
        result = day23.solve('916438275', 2)
        self.assertEqual(result, 149245887792)
#     def test_in(self):
#         result = day23.solve('916438275', 2)
#         self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main(verbosity=2)