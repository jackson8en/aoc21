import unittest
from aoc.sonar_sweep import *


class TestSonarSweep(unittest.TestCase):
    def test_example(self):
        data = ""
        with open("./data/sonar_sweep_e.dat") as raw_data:
            data = raw_data.readlines()
        result = sonar_sweep(data)
        print(result)
        self.assertEqual(7, result)

    def test_stage_1(self):
        data = ""
        with open("./data/sonar_sweep_1.dat") as raw_data:
            data = raw_data.readlines()
        result = sonar_sweep(data)
        print(result)
        self.assertEqual(1228, result)


class TestSonarSweepWindow(unittest.TestCase):
    def test_example(self):
        data = ""
        with open("./data/sonar_sweep_e.dat") as raw_data:
            data = raw_data.readlines()
        result = sonar_sweep_window(data, window=3)
        print(result)
        self.assertEqual(5, result)

    def test_stage_1(self):
        data = ""
        with open("./data/sonar_sweep_1.dat") as raw_data:
            data = raw_data.readlines()
        result = sonar_sweep_window(data, window=3)
        print(result)
        self.assertEqual(1257, result)
