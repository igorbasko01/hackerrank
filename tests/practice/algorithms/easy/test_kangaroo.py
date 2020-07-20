import unittest
from practice.algorithms.easy.kangaroo import kangaroo


class KangarooTest(unittest.TestCase):
    def test_sample(self):
        result = kangaroo(0, 3, 4, 2)
        self.assertEqual('YES', result)

    def test_sample1(self):
        result = kangaroo(0, 2, 5, 3)
        self.assertEqual('NO', result)

    def test_sample2(self):
        result = kangaroo(21, 6, 47, 3)
        self.assertEqual('NO', result)

    def test_sample3(self):
        result = kangaroo(43, 5, 49, 3)
        self.assertEqual('YES', result)

    def test_sample4(self):
        result = kangaroo(43, 2, 70, 2)
        self.assertEqual('NO', result)
