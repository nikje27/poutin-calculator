import unittest
import calc

class TestCalc(unittest.TestCase):

  def test_multiply(self):
          self.assertEqual(calc.multiply(10, 5), 50)
          self.assertEqual(calc.multiply(-1, 1), -1)
          self.assertEqual(calc.multiply(-1, -1), 1)

if __name__ == '__main__':
    unittest.main()
