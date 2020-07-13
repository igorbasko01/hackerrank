import unittest
from challenges.warm_up.counting_valleys import counting_valleys


class CountingVallyesTest(unittest.TestCase):
    def test_sample(self):
        result = counting_valleys(8, 'UDDDUDUU')
        self.assertEqual(result, 1)

    def test_sample1(self):
        result = counting_valleys(8, 'DDUUUUDD')
        self.assertEqual(result, 1)

    def test_sample2(self):
        result = counting_valleys(12, 'DDUUDDUDUUUD')
        self.assertEqual(result, 2)
