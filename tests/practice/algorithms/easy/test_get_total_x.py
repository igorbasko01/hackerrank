import unittest
from practice.algorithms.easy.get_total_x import get_total_x


class GetTotalXTest(unittest.TestCase):
    def test_sample(self):
        result = get_total_x([2, 6], [24, 36])
        self.assertEqual(2, result)

    def test_sample1(self):
        result = get_total_x([2, 4], [16, 32, 96])
        self.assertEqual(3, result)
