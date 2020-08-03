import unittest
from practice.algorithms.easy.birthday import birthday


class BirthdayTest(unittest.TestCase):
    def test_sample(self):
        arr = [1, 2, 1, 3, 2]
        d = 3
        m = 2
        result = birthday(arr, d, m)
        self.assertEqual(2, result)

    def test_sample2(self):
        arr = [1, 1, 1, 1, 1, 1]
        d = 3
        m = 2
        result = birthday(arr, d, m)
        self.assertEqual(0, result)

    def test_sample3(self):
        arr = [4]
        d = 4
        m = 1
        result = birthday(arr, d, m)
        self.assertEqual(1, result)

    def test_sample4(self):
        arr = [2, 2, 2, 2, 2, 2, 2]
        d = 4
        m = 2
        result = birthday(arr, d, m)
        self.assertEqual(6, result)
