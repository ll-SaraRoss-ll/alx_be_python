import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        """Create a new calculator before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test add with integers, negatives, and floats."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, -1), -2)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertAlmostEqual(self.calc.add(2.5, 3.1), 5.6)

    def test_subtraction(self):
        """Test subtract with various inputs."""
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(5, 10), -5)
        self.assertAlmostEqual(self.calc.subtract(2.5, 1.2), 1.3)

    def test_multiplication(self):
        """Test multiply including zero and negative factors."""
        self.assertEqual(self.calc.multiply(4, 5), 20)
        self.assertEqual(self.calc.multiply(0, 100), 0)
        self.assertEqual(self.calc.multiply(-3, 7), -21)
        self.assertAlmostEqual(self.calc.multiply(2.5, 4), 10.0)

    def test_division_normal(self):
        """Test divide under normal conditions."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)
        self.assertAlmostEqual(self.calc.divide(-9, 3), -3)

    def test_division_by_zero(self):
        """Test that dividing by zero returns None."""
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertIsNone(self.calc.divide(0, 0))

    def test_division_with_floats(self):
        """Test divide with floating-point values."""
        result = self.calc.divide(5.5, 2.2)
        self.assertAlmostEqual(result, 2.5)

if __name__ == '__main__':
    unittest.main()
