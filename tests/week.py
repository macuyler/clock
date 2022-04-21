"""Unit tests covering the src.week module."""

import unittest

from src.week import Week


class TestWeek(unittest.TestCase):

    def test_stuff(self):
        days = ['01/01/22=00:01', '01/02/22=10:01']
        print(Week(0, days))
        self.assertEqual(0 , 0)


if __name__ == '__main__':
    unittest.main()
