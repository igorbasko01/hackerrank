import unittest
from practice.algorithms.easy.time_conversion import time_conversion


class TimeConversionTest(unittest.TestCase):
    def test_sample(self):
        result = time_conversion("07:05:45PM")
        self.assertEqual("19:05:45", result)

    def test_sample2(self):
        result = time_conversion("07:05:45AM")
        self.assertEqual("07:05:45", result)

    def test_sample3(self):
        result = time_conversion("12:05:45AM")
        self.assertEqual("00:05:45", result)

    def test_sample4(self):
        result = time_conversion("12:45:54PM")
        self.assertEqual("12:45:54", result)
