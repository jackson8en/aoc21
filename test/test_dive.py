import unittest
from aoc.dive import *


class TestDive(unittest.TestCase):
    def test_example(self):
        data = ""
        with open("./data/dive_e.dat") as raw_data:
            data = raw_data.readlines()
        pos = dive(data)
        result = pos[0] * pos[1]
        print(pos, result)
        self.assertEqual(150, result)

    def test_stage_1(self):
        data = ""
        with open("./data/dive_1.dat") as raw_data:
            data = raw_data.readlines()
        pos = dive(data)
        result = pos[0] * pos[1]
        print(result)
        self.assertEqual(1855814, result)


class TestAdvancedDive(unittest.TestCase):
    def test_example(self):
        data = ""
        with open("./data/dive_e.dat") as raw_data:
            data = raw_data.readlines()
        pos = adv_dive(data)
        result = pos[0] * pos[1]
        print(pos, result)
        self.assertEqual(900, result)

    def test_stage_1(self):
        data = ""
        with open("./data/dive_1.dat") as raw_data:
            data = raw_data.readlines()
        pos = adv_dive(data)
        result = pos[0] * pos[1]
        print(result)
        self.assertEqual(1845455714, result)
