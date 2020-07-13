import unittest
from challenges.arrays.left_rotation import rot_left


class LeftRotationTest(unittest.TestCase):
    def test_sample(self):
        result = rot_left([1, 2, 3, 4, 5], 4)
        self.assertEqual([5, 1, 2, 3, 4], result)

    def test_sample1(self):
        result = rot_left([1], 4)
        self.assertEqual([1], result)

    def test_sample2(self):
        result = rot_left([], 4)
        self.assertEqual([], result)

    def test_sample3(self):
        result = rot_left([1, 2, 3, 4, 5], 0)
        self.assertEqual([1, 2, 3, 4, 5], result)
