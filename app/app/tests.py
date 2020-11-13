from django.test import TestCase

from app.calc import add, subtract


class CalcTests(TestCase):

    def test_add_numbers(self):
        """
        Test that two numbers are added together
        :return:
        """
        self.assertEqual(add(3, 5), 8)

    def test_subtract_numbers(self):
        """
        Test that two numbers are subtracted together
        :return:
        """
        self.assertEqual(subtract(3, 5), 2)
