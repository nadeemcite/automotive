from unittest import TestCase
from automation.sample_code import sample_code

class TestSampleCode(TestCase):
    def test_sample_code(self):
        self.assertTrue(sample_code(4, 5), 9)