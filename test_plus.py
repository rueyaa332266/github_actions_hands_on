import unittest
from plus import plus

class TestPlus(unittest.TestCase):

    def test_plus_1(self):
        self.assertEqual(2, plus(1, 1))

    def test_plus_2(self):
        self.assertEqual(0, plus(-1, 1))
    
    def test_plus_3(self):
        self.assertEqual(1, plus(1, 2))

if __name__ == "__main__":
    unittest.main()