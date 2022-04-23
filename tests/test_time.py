"""Unit tests covering the src.time module."""

import unittest

from src.time import hmt, str_to_time


class TestTime(unittest.TestCase):

    def test_string_to_time(self):
        result = str_to_time('10:10')
        expected = hmt(10, 10)
        msg = 'Time should be parsed from a string.'
        self.assertEqual(result, expected, msg)

        result = str_to_time('1:30')
        expected = None
        msg = 'None should be returned if the string has a bad format.'
        self.assertEqual(result, expected, msg)


    def test_time_to_string(self):
        result = str(hmt(1, 1))
        expected = '01:01'
        msg = 'Single digit time values should be padded with a 0.'
        self.assertEqual(result, expected, msg)
