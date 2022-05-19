"""Unit tests covering the src.parse module."""

import unittest
from typing import Callable

from src.parse import get_pattern, int_parser, parse


class TestParse(unittest.TestCase):

    def test_get_pattern(self):
        fmt = '%M/%D/%Y'
        result = get_pattern(fmt)
        expected = [int_parser(1, 12), '/', int_parser(1, 31), '/', int_parser(0, 99)]
        msg = 'Format strings should be parsed to generate a pattern.'
        self.assertTrue(parsers_match(result[0], expected[0], range(0, 14)), msg)
        self.assertEqual(result[1], expected[1], msg)
        self.assertTrue(parsers_match(result[2], expected[2], range(0, 33)), msg)
        self.assertEqual(result[3], expected[3], msg)
        self.assertTrue(parsers_match(result[4], expected[4], range(-1, 101)), msg)


    def test_pattern_prefix(self):
        fmt = 'Prefix: %M/%D/%Y'
        result = get_pattern(fmt)
        expected = ['Prefix: ', int_parser(1, 12), '/', int_parser(1, 31), '/', int_parser(0, 99)]
        msg = 'Format parsing should retain any prefix content.'
        self.assertEqual(result[0], expected[0], msg)
        self.assertTrue(parsers_match(result[1], expected[1], range(0, 14)), msg)
        self.assertEqual(result[2], expected[2], msg)
        self.assertTrue(parsers_match(result[3], expected[3], range(0, 33)), msg)
        self.assertEqual(result[4], expected[4], msg)
        self.assertTrue(parsers_match(result[5], expected[5], range(-1, 101)), msg)


    def test_pattern_suffix(self):
        fmt = '%M/%D/%Y suffix...'
        result = get_pattern(fmt)
        expected = [int_parser(1, 12), '/', int_parser(1, 31), '/', int_parser(0, 99), ' suffix...']
        msg = 'Format parsing should retain any suffix content.'
        self.assertTrue(parsers_match(result[0], expected[0], range(0, 14)), msg)
        self.assertEqual(result[1], expected[1], msg)
        self.assertTrue(parsers_match(result[2], expected[2], range(0, 33)), msg)
        self.assertEqual(result[3], expected[3], msg)
        self.assertTrue(parsers_match(result[4], expected[4], range(-1, 101)), msg)
        self.assertEqual(result[5], expected[5], msg)


    def test_valid_value(self):
        fmt = '%M/%D/%Y=%h:%m'
        val = '01/01/01=01:01'

        month, day, year, hours, mins = parse(fmt, val)
        msg = 'Parse should return values according to a pattern.'

        self.assertEqual(month, 1, msg)
        self.assertEqual(day, 1, msg)
        self.assertEqual(year, 1, msg)
        self.assertEqual(hours, 1, msg)
        self.assertEqual(mins, 1, msg)


    def test_invalid_value(self):
        fmt = '%M/%D/%Y'
        val = 'JAN/0/2001'

        month, day, year = parse(fmt, val)
        msg = 'None should be returned for invalid values.'

        self.assertEqual(month, None, msg)
        self.assertEqual(day, None, msg)
        self.assertEqual(year, None, msg)


    def test_invalid_delim(self):
        fmt = '%M/%D/%Y'
        val = '01|01|01'

        month, day, year = parse(fmt, val)
        msg = 'None should be returned when value uses invalid formatting.'

        self.assertEqual(month, None, msg)
        self.assertEqual(day, None, msg)
        self.assertEqual(year, None, msg)


    def test_parse_with_prefix(self):
        fmt = 'Prefix: %M/%D/%Y'
        val = 'Prefix: 01/01/01'

        month, day, year = parse(fmt, val)
        msg = 'Parse should only handle data after the prefix.'

        self.assertEqual(month, 1, msg)
        self.assertEqual(day, 1, msg)
        self.assertEqual(year, 1, msg)


    def test_parse_with_suffix(self):
        fmt = '%M/%D/%Y, suffix.'
        val = '01/01/01, suffix.'

        month, day, year = parse(fmt, val)
        msg = 'Parse should only handle data behind the suffix.'

        self.assertEqual(month, 1, msg)
        self.assertEqual(day, 1, msg)
        self.assertEqual(year, 1, msg)


    def test_parsed_values_success(self):
        fmt = '%M/%D/%Y'

        result = parse(fmt, '02/03/04')
        msg = 'ParsedValues.success should return True if all values were parsed.'
        self.assertTrue(result.success, msg)

        result = parse(fmt, '')
        msg = 'ParsedValues.success should return False if any values were not parsed.'
        self.assertFalse(result.success, msg)


def parsers_match(parser: Callable, control: Callable, nums: range) -> bool:
    """Test that the output of a parser matches that of a control parser for a range of inputs."""

    match = True

    for i in nums:
        val = str(i)
        result = parser(val)
        expected = control(val)

        if result != expected:
            match = False

    return match


if __name__ == '__main__':
    unittest.main()
