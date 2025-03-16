from unittest import TestCase
from automation.sample_code import add_two_numbers

class TestSampleCode(TestCase):
    def test_sample_code(self):
        self.assertEqual(add_two_numbers(4, 5), 9)