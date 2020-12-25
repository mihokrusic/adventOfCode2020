#!/usr/bin/env python3
import unittest
import os

os.sys.path.insert(0, os.getcwd())

from solutions import day25

class Part1(unittest.TestCase):
    def test_01(self):
        result = day25.solve(5764801, 17807724)
        self.assertEqual(result, 14897079)
    def test_in(self):
        result = day25.solve(8252394, 6269621)
        self.assertEqual(result, 181800)

if __name__ == '__main__':
    unittest.main(verbosity=2)

