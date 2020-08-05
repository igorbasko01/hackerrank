import unittest
from practice.algorithms.easy.divisible_sum_pairs import divisible_sum_pairs


class DivisibleSumPairsTest(unittest.TestCase):
    def test_sample(self):
        result = divisible_sum_pairs(6, 3, [1, 3, 2, 6, 1, 2])
        self.assertEqual(5, result)

    def test_sample1(self):
        result = divisible_sum_pairs(6, 5, [1, 2, 3, 4, 5, 6])
        self.assertEqual(3, result)
