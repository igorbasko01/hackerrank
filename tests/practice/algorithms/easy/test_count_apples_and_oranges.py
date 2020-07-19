import unittest
from practice.algorithms.easy.count_apples_and_oranges import count_apples_and_oranges


class CountApplesAndOrangesTest(unittest.TestCase):
    def test_sample(self):
        result = count_apples_and_oranges(7, 11, 5, 15, [-2, 2, 1], [5, -6])
        self.assertEqual([1, 1], result)
