import unittest
from challenges.warm_up.jumping_on_clouds import jumping_on_clouds


class JumpingOnCloudsTest(unittest.TestCase):
    def test_sample(self):
        result = jumping_on_clouds([0, 0, 1, 0, 0, 1, 0])
        self.assertEqual(result, 4)

    def test_sample1(self):
        result = jumping_on_clouds([0, 0, 0, 0, 1, 0])
        self.assertEqual(result, 3)
