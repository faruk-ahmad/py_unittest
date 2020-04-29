import unittest
import sys
sys.path.append('..')

from myapp.utils import division, addition

class TestAddition(unittest.TestCase):
    def setup(self):
        pass

    def tear_down(self):
        pass

    def test_additions(self):
        self.assertEqual(addition(10, 5), 15, 'Failed to add 10 and 5')
        self.assertEqual(addition(0, 4), 4, 'Failed to add 0 and 4')
        self.assertEqual(addition(4, 0), 4, 'Failed to add 4 and 0')
        self.assertEqual(addition(-1, 0), -1, 'Failed to add -1 and 0')


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
