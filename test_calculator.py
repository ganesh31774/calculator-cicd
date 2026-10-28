import unittest
from calculator import add,subtract,multiply,devide

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add(10, 5),15)

    def test_subtraction(self):
        self.assertEqual(subtract(10, 5),5)

    def test_multiplaction(self):
         self.assertEqual(multiply(10, 5),50)

    def test_division(self):
            self.assertEqual(devide(10, 5),2.0)
    def test_division_by_zero(self):
         with self.assertRaises(ValueError):
              devide(10,0)
if __name__ == "__main__":
     unittest.main()
     
