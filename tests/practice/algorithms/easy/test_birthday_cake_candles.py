import unittest
from practice.algorithms.easy.birthday_cake_candles import birthday_cake_candles
from practice.algorithms.easy.birthday_cake_candles import short_solution


class BirthdayCakeCandlesTest(unittest.TestCase):
    def test_sample(self):
        arr = [3, 2, 1, 3]
        result = birthday_cake_candles(arr)
        result2 = short_solution(arr)
        self.assertEqual(2, result)
        self.assertEqual(2, result2)

    def test_sample2(self):
        arr = [4, 4, 1, 3]
        result = birthday_cake_candles(arr)
        result2 = short_solution(arr)
        self.assertEqual(2, result)
        self.assertEqual(2, result2)
