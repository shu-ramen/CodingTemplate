import sys
sys.path.append("../src")

import unittest
import mymodule

class TestMymodule(unittest.TestCase):
    """test class of mymodule.py
    """
    
    def setUp(self):
        print("setup")
        self.eq1 = mymodule.QudraticEquations(1.0, 3.0, 2.0)
        self.eq2 = mymodule.QudraticEquations(1.0, 2.0, 1.0)
        self.eq3 = mymodule.QudraticEquations(1.0, 2.0, 5.0)

    def test_calc_sum(self):
        """test method for calc_sum
        """
        self.assertEqual(8, mymodule.calc_sum(2, 6))
    
    def test_calc_root(self):
        """test method for calc_root
        """
        self.assertEqual("-1.0, -2.0", self.eq1.calc_root())
        self.assertEqual("-1.0", self.eq2.calc_root())
        self.assertEqual("-1.0 + i(2.0), -1.0 - i(2.0)", self.eq3.calc_root())
        
    def test_calc_value(self):
        """test method for calc_value
        """
        self.assertEqual(0.0, self.eq1.calc_value(-1))
        self.assertEqual(0.0, self.eq2.calc_value(-1))
        self.assertEqual(4.0, self.eq3.calc_value(-1))

    def tearDown(self):
        print("tearDown")
        del self.eq1
        del self.eq2
        del self.eq3

if __name__ == "__main__":
    unittest.main()