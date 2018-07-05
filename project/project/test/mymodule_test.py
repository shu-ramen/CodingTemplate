import sys
sys.path.append("../src")

import unittest
import mymodule

class TestCalcSum(unittest.TestCase):
    """test class of tashizan.py
    """

    def test_calc_sum(self):
        """test method for calc_sum
        """
        value1 = 2
        value2 = 6
        expected = 8
        actual = mymodule.calc_sum(value1, value2)
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()