import unittest
from Perceptron.PerceptronClass import *


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.andpercept = AND()
        self.orpercept = OR()
        self.nandpercept = NAND()

    def test_AND(self):
        self.assertFalse(self.andpercept.feed([0, 0]))
        self.assertFalse(self.andpercept.feed([0, 1]))
        self.assertFalse(self.andpercept.feed([1, 0]))
        self.assertTrue(self.andpercept.feed([1, 1]))

    def test_OR(self):
        self.assertFalse(self.orpercept.feed([0, 0]))
        self.assertTrue(self.orpercept.feed([0, 1]))
        self.assertTrue(self.orpercept.feed([1, 0]))
        self.assertTrue(self.orpercept.feed([1, 1]))

    def test_NAND(self):
        self.assertTrue(self.nandpercept.feed([0, 0]))
        self.assertTrue(self.nandpercept.feed([0, 1]))
        self.assertTrue(self.nandpercept.feed([1, 0]))
        self.assertFalse(self.nandpercept.feed([1, 1]))


if __name__ == '__main__':
    unittest.main()
