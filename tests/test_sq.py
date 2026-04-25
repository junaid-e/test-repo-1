import unittest

#I have called the class "SmokeTest. It is using unittest.TestCase from the unittest import.
class SmokeTest(unittest.TestCase):
    def test2_and_2(self):
        self.assertEqual(2+2,4)

if __name__ == "__main__":
    unittest.main()
    