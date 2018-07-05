import sys
sys.path.append("../src")

import unittest
import mymodule

class TestMymodule(unittest.TestCase):
    """test class of mymodule.py
    """

    def test_calc_sum(self):
        """test method for calc_sum
        """
        expected = 8
        actual = mymodule.calc_sum(2, 6)
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()