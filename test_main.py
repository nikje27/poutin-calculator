from unittest import TestCase
from main import divide, add, multiply, subtract

class TestCalc(TestCase):

    def test_divide(self):
        self.assertEqual(divide(10, 5), 2)
        self.assertEqual(divide(-1, 1), -1)
        self.assertEqual(divide(-1, -1), 1)
        self.assertEqual(divide(5, 2), 2.5)

        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_multiply(self):
        self.assertEqual(main.multiply(10, 5), 50)
        self.assertEqual(main.multiply(-1, 1), -1)
        self.assertEqual(main.multiply(-1, -1), 1)

    def test_add(self):
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)
