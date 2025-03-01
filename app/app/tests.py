'''
Sample test cases for the app
'''

from django.test import SimpleTestCase 

from app import calc

class CalcTests(SimpleTestCase):
    def test_add(self):
        self.assertEqual(calc.add(2, 3), 5)

    def test_multiply(self):
        self.assertEqual(calc.multiply(3, 4), 12)