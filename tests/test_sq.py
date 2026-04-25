import unittest
from roots import sq_num

#I have called the class "SmokeTest. It is using unittest.TestCase from the unittest import.
class SmokeTest(unittest.TestCase):
    def test2_and_2(self):
        self.assertEqual(2+2,4)

class TestSquare(unittest.TestCase):
    def test_root_of_0(self):
        self.assertEqual(sq_num(0),0)

if __name__ == "__main__":
    unittest.main()
    