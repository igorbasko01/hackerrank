import unittest
from practice.algorithms.easy.plus_minus import plus_minus


class PlusMinusTest(unittest.TestCase):
    def test_sample(self):
        result = plus_minus([-4, 3, -9, 0, 4, 1])
        self.assertEqual([0.500000, 0.333333, 0.166667], result)
