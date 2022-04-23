"""Unit tests covering the src.week module."""

import unittest

from src.time import hmt
from src.week import Week


class TestWeek(unittest.TestCase):

    def test_total(self):
        msg = 'The total hours logged in a week should be calculated.'
        week_num = 12

        days = ['04/24/22=01:01',
                '04/25/22=03:23',
                '04/26/22=00:30',
                '04/27/22=05:03',
                '04/28/22=02:10',
                '04/29/22=10:45',
                '04/30/22=08:32']

        result = Week(week_num, days).total
        expected = hmt(31, 24)
        self.assertEqual(result, expected, msg)

        result = Week(week_num, days)
        expected = '\n'.join([f'- Week {week_num}:', *days, '-- Total=31:24'])
        self.assertEqual(str(result), expected, msg)

        days = ['05/01/22=90:30',
                '05/02/22=95:30',
                '05/03/22=95:30',
                '05/04/22=95:30']

        result = Week(week_num, days).total
        expected = hmt(377, 0)
        self.assertEqual(result, expected, msg)



if __name__ == '__main__':
    unittest.main()
