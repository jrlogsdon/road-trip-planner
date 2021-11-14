import unittest
import time_to_date_time_converter
from datetime import timedelta


#Likely don't need, didn't realize a value was already associated in the json
class MyTestCase(unittest.TestCase):
    def test_minutes(self):
        input = '33 mins'
        actual = time_to_date_time_converter.convert(input)
        expected = timedelta(minutes=33)
        self.assertEqual(expected, actual)


    def test_hours(self):
        input = '13 hours'
        actual = time_to_date_time_converter.convert(input)
        expected = timedelta(hours=13)
        self.assertEqual(expected, actual)


    def test_day_hour(self):
        input = '1 day 10 hours'
        actual = time_to_date_time_converter.convert(input)
        expected = timedelta(days=1, hours=10)
        self.assertEqual(expected, actual)

    def test_hour_and_mins(self):
        input = '13 hours 32 mins'
        actual = time_to_date_time_converter.convert(input)
        expected = timedelta(days=0, hours=13, minutes=32)
        self.assertEqual(expected, actual)

    def test_convert(self):
        expected = 5
        actual = int(' 5')
        self.assertEqual(expected, actual)
