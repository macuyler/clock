"""Unit tests covering the src.time module."""

import unittest
from datetime import timedelta

from src.time import delta_to_time, hmt


class TestTime(unittest.TestCase):


    def test_time_to_string(self):
        result = str(hmt(1, 1))
        expected = '01:01'
        msg = 'Single digit time values should be padded with a 0.'
        self.assertEqual(result, expected, msg)


    def test_delta_to_time(self):
        result = delta_to_time(timedelta(seconds=31))
        expected = hmt(0, 1)
        msg = 'Deltas over 30 seconds should be rounded up to a minute.'
        self.assertEqual(result, expected, msg)

        result = delta_to_time(timedelta(seconds=30))
        expected = hmt(0, 0)
        msg = 'Deltas of 30 seconds or less should be rounded down to 0.'
        self.assertEqual(result, expected, msg)

        result = delta_to_time(timedelta(days=1))
        expected = hmt(24, 0)
        msg = 'Time deltas should be properly converted into Time objects.'
        self.assertEqual(result, expected, msg)
