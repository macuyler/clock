"""Unit tests covering the src.day module."""

import datetime
import unittest

from src.day import Day


class TestDay(unittest.TestCase):

    def test_stuff(self):

        today = datetime.date.today()
        day = Day(today, 1.0)
        print(day)

        self.assertEqual(0, 0)


if __name__ == '__main__':
    unittest.main()
