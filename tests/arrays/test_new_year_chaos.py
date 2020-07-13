import unittest
from challenges.arrays.new_year_chaos import minimum_bribes


class NewYearChaosTest(unittest.TestCase):
    def test_sample(self):
        result = minimum_bribes([2, 1, 5, 3, 4])
        self.assertEqual(3, result)

    def test_sample1(self):
        result = minimum_bribes([1, 2, 5, 3, 7, 8, 6, 4])
        self.assertEqual(7, result)

    def test_sample2(self):
        result = minimum_bribes([1, 2, 5, 3, 4, 7, 8, 6])
        self.assertEqual(4, result)

    def test_sample_chaos(self):
        result = minimum_bribes([2, 5, 1, 3, 4])
        self.assertEqual('Too chaotic', result)