import unittest
from knows_basics import sum_digits

class TestSumDigits(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(sum_digits(123), 6)
        self.assertEqual(sum_digits(9876), 30)
    
    def test_single_digit(self):
        self.assertEqual(sum_digits(5), 5)
        self.assertEqual(sum_digits(0), 0)
    
    def test_negative_numbers(self):
        self.assertEqual(sum_digits(-456), 15)
    
    def test_large_number(self):
        self.assertEqual(sum_digits(123456789), 45)
    
if __name__ == "__main__":
    unittest.main()