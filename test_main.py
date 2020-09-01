import unittest
from main import add


class TestCalc(unittest.TestCase):  # test case
    """
    Unit test for basic arithmetic operations
    Credits: https://github.com/CoreyMSchafer/code_snippets/tree/master/Python-Unit-Testing
    """

    def test_add(self):
        self.assertEqual(main.add(10, 5), 15)
        self.assertEqual(main.add(-1, 1), 0)
        self.assertEqual(main.add(-1, -1), -2)




if __name__ == '__main__':
    unittest.main()