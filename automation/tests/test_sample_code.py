from unittest import TestCase
from automation.sample_code import add_two_numbers

class TestSampleCode(TestCase):
    def test_sample_code(self):
        self.assertEqual(add_two_numbers(4, 5), 9)

    def test_positive_numbers(self):
        # Additional regular cases
        self.assertEqual(add_two_numbers(1, 1), 2)
        self.assertEqual(add_two_numbers(10, 20), 30)
        self.assertEqual(add_two_numbers(100, 1), 101)

    def test_zero_handling(self):
        # Test with zero (assuming it's considered non-negative)
        self.assertEqual(add_two_numbers(0, 5), 5)
        self.assertEqual(add_two_numbers(5, 0), 5)
        self.assertEqual(add_two_numbers(0, 0), 0)

    def test_negative_numbers(self):
        # Test negative number validation
        with self.assertRaises(ValueError):
            add_two_numbers(-1, 5)
        with self.assertRaises(ValueError):
            add_two_numbers(5, -1)
        with self.assertRaises(ValueError):
            add_two_numbers(-1, -1)

    def test_large_numbers(self):
        # Test with large integers
        self.assertEqual(add_two_numbers(1000000, 2000000), 3000000)
        # Test near system max int if relevant to requirements
        large_number = sys.maxsize // 2
        self.assertEqual(add_two_numbers(large_number, large_number), large_number * 2)