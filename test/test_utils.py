import unittest
import sys
sys.path.append('..')

from myapp.utils import division


class TestDivision(unittest.TestCase):
    def setup(self):
        pass

    def tear_down(self):
        pass

    def test_divitions(self):
        self.assertEqual(division(10, 2), 5, 'Failed to divide 10 by 2')
        self.assertEqual(division(100, 5), 20, 'Failed to divide 100 by 5')
        self.assertEqual(division(100, 1), 100, 'Failed to divide 100 by 1')

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            division(10, 0)