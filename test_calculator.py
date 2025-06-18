import unittest
from calculator import add, subtract, multiply, divide, sqrt # Assuming calculator.py is in the same directory or PYTHONPATH

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(10.5, 2.5), 13.0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(-1, -1), 0)
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(5.5, 2.5), 3.0)

    def test_multiply(self):
        self.assertEqual(multiply(3, 2), 6)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(-1, -1), 1)
        self.assertEqual(multiply(0, 100), 0)
        self.assertEqual(multiply(3.5, 2.0), 7.0)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(-10, 2), -5)
        self.assertEqual(divide(-10, -2), 5)
        self.assertEqual(divide(0, 1), 0)
        self.assertEqual(divide(5, 2), 2.5)

        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_sqrt(self):
        self.assertEqual(sqrt(4), 2)
        self.assertEqual(sqrt(9.0), 3.0)
        self.assertEqual(sqrt(0), 0)
        self.assertAlmostEqual(sqrt(2), 1.41421356, places=7) # Test with a non-perfect square

        with self.assertRaises(ValueError):
            sqrt(-1)
        with self.assertRaises(ValueError):
            sqrt(-100)

if __name__ == '__main__':
    unittest.main()
