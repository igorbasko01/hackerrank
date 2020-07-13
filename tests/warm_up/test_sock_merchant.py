import unittest
from challenges.warm_up.sock_merchant import sock_merchant


class SockMerchantTest(unittest.TestCase):
    def test_sample(self):
        result = sock_merchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20])
        self.assertEqual(result, 3)

    def test_sample2(self):
        result = sock_merchant(10, [1, 1, 3, 1, 2, 1, 3, 3, 3, 3])
        self.assertEqual(result, 4)


if __name__ == '__main__':
    unittest.main()
