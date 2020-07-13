import unittest
from challenges.warm_up.repeated_string import repeated_string, repeated_string_not_mine


class RepeatedStringTest(unittest.TestCase):
    def test_sample(self):
        result = repeated_string('aba', 10)
        self.assertEqual(result, 7)

    def test_sample1(self):
        result = repeated_string('a', 1000000000000)
        self.assertEqual(result, 1000000000000)

    def test_sample_not_mine(self):
        result = repeated_string_not_mine('aba', 10)
        self.assertEqual(result, 7)

    def test_sample_not_mine1(self):
        result = repeated_string_not_mine('a', 1000000000000)
        self.assertEqual(result, 1000000000000)
