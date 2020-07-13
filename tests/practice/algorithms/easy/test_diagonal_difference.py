import unittest
from practice.algorithms.easy.diagonal_difference import diagonal_diff


class DiagonalDifferenceTest(unittest.TestCase):
    def test_sample(self):
        result = diagonal_diff([[11, 2, 4],
                                [4, 5, 6],
                                [10, 8, -12]])
        self.assertEqual(15, result)
