import unittest
from practice.algorithms.easy.breaking_records import breaking_records


class BreakingRecordsTest(unittest.TestCase):
    def test_sample(self):
        result = breaking_records([10, 5, 20, 20, 4, 5, 2, 25, 1])
        self.assertEqual([2, 4], result)

    def test_sample1(self):
        result = breaking_records([3, 4, 21, 36, 10, 28, 35, 5, 24, 42])
        self.assertEqual([4, 0], result)
