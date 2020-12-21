#!/usr/bin/env python3
import unittest
import os

os.sys.path.insert(0, os.getcwd())

from solutions import day21
from utility import inputs

class Part1(unittest.TestCase):
    def test_01(self):
        result = day21.solve(inputs.read_str("input21"), 1)
        self.assertEqual(result, 5)
    def test_in(self):
        result = day21.solve(inputs.read_str("input21_actual"), 1)
        self.assertEqual(result, 2595)

class Part2(unittest.TestCase):
    def test_01(self):
        result = day21.solve(inputs.read_str("input21"), 2)
        self.assertEqual(result, 'mxmxvkd,sqjhc,fvjkl')
    def test_in(self):
        result = day21.solve(inputs.read_str("input21_actual"), 2)
        self.assertEqual(result, 'thvm,jmdg,qrsczjv,hlmvqh,zmb,mrfxh,ckqq,zrgzf')

if __name__ == '__main__':
    unittest.main(verbosity=2)