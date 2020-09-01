import unittest
from main import multiply

class TestCalc(unittest.TestCase):

  def test_multiply(self):
          self.assertEqual(main.multiply(10, 5), 50)
          self.assertEqual(main.multiply(-1, 1), -1)
          self.assertEqual(main.multiply(-1, -1), 1)

if __name__ == '__main__':
    unittest.main()
