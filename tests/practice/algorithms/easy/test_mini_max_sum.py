import unittest
from practice.algorithms.easy.mini_max_sum import mini_max_sum


class MiniMaxSumTest(unittest.TestCase):
    def test_sample(self):
        result = mini_max_sum([1, 2, 3, 4, 5])
        self.assertEqual([10, 14], result)
