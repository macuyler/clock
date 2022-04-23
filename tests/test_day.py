"""Unit tests covering the src.day module."""

import datetime
import unittest

from src.day import Day, str_to_day
from src.time import Time, hmt


class TestDay(unittest.TestCase):

    def test_day_to_string(self):
        msg = 'Days should be formatted when converted to a string.'

        result = str(Day(datetime.date(2020, 12, 31), hmt(12, 30)))
        expected = '12/31/20=12:30'
        self.assertEqual(result, expected, msg)

        result = str(Day(datetime.date(2000, 2, 1), hmt(1, 7)))
        expected = '02/01/00=01:07'
        self.assertEqual(result, expected, msg)


    def test_string_to_day(self):
        result = str_to_day('04/20/22=06:35')
        expected = Day(datetime.date(2022, 4, 20), hmt(6, 35))
        msg = 'Strings should be parsed into Days.'
        self.assertEqual(result.date, expected.date, msg)
        self.assertEqual(result.time, expected.time, msg)

        result = str_to_day('wednesday')
        expected = None
        msg = 'None should be returned when parsing invalid strings.'
        self.assertEqual(result, expected, msg)


if __name__ == '__main__':
    unittest.main()
