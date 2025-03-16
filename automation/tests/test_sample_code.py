from unittest import TestCase
from automation.sample_code import sum

class TestSampleCode(TestCase):
    def test_sample_code(self):
        self.assertEqual(sum(4, 5), 9)