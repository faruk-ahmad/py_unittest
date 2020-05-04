import unittest
import sys

sys.path.append('..')

from myapp.calculator import Calculator


class TestCalculator(unittest.TestCase):
    """ A class to test Calculator class """

    def setUp(self):
        self.cal = Calculator()


    def test_add(self):
        self.assertEqual(self.cal.add(5, 6), 11, "addition of 5, 6 not correct")