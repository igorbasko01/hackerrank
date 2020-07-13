import unittest
from challenges.arrays.two_d_array_ds import hourglass_sum


class TwoDArrayTest(unittest.TestCase):
    def test_sample(self):
        result = hourglass_sum([[1, 1, 1, 0, 0, 0],
                                [0, 1, 0, 0, 0, 0],
                                [1, 1, 1, 0, 0, 0],
                                [0, 0, 2, 4, 4, 0],
                                [0, 0, 0, 2, 0, 0],
                                [0, 0, 1, 2, 4, 0]])
        self.assertEqual(19, result)

    def test_sample1(self):
        result = hourglass_sum([[-1, -1, 0, -9, -2, -2],
                                [-2, -1, -6, -8, -2, -5],
                                [-1, -1, -1, -2, -3, -4],
                                [-1, -9, -2, -4, -4, -5],
                                [-7, -3, -3, -2, -9, -9],
                                [-1, -3, -1, -2, -4, -5]])

        self.assertEqual(-6, result)
