import unittest
from practice.algorithms.easy.grading_students import grading_students


class GradingStudentsTest(unittest.TestCase):
    def test_sample(self):
        result = grading_students([73, 67, 38, 33])
        self.assertEqual([75, 67, 40, 33], result)
