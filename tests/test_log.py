"""Unit tests covering the src.log module."""

import unittest
from pathlib import Path

from src.log import Log
from src.week import Week

from tests import setup


class TestLog(unittest.TestCase):

    def test_load(self):
        log_path = f'{Path.home()}/clock-test-log.txt'
        log_content = """
        01/08/01=01:00
        01/08/01=01:00
        01/08/01=03:00
        01/09/01=00:00
        01/10/01=00:00
        01/11/01=00:00
        -- Total=00:00
        - Week 1:
        -- Total=00:00
        01/07/01=00:00
        01/06/01=00:00
        01/05/01=00:00
        01/04/01=00:00
        01/03/01=00:00
        01/02/01=00:00
        01/01/01=00:00
        - Week 0:
        12/25/00=00:00
        nonsense...
        :)
        """

        setup((log_path, log_content))

        week1 = ['12/25/00=00:00',
                 '12/26/00=00:00',
                 '12/27/00=00:00',
                 '12/28/00=00:00',
                 '12/29/00=00:00',
                 '12/30/00=00:00',
                 '12/31/00=00:00']
        week2 = ['01/01/01=00:00',
                 '01/02/01=00:00',
                 '01/03/01=00:00',
                 '01/04/01=00:00',
                 '01/05/01=00:00',
                 '01/06/01=00:00',
                 '01/07/01=00:00']
        week3 = ['01/08/01=05:00',
                 '01/09/01=00:00',
                 '01/10/01=00:00',
                 '01/11/01=00:00']

        result = Log(Path(log_path)).weeks
        expected = [Week(1, week1), Week(2, week2), Week(3, week3)]
        msg = 'Logs should be parsed and organized into weeks.'
        self.assertEqual(result, expected, msg)


if __name__ == '__main__':
    unittest.main()