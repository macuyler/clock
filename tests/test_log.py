"""Unit tests covering the src.log, src.log_data, and src.log_tools module."""

import unittest

from src.log import LogData, parse_log
from src.time import hmt
from src.week import Week


class TestLog(unittest.TestCase):

    def test_parse_log(self):
        log_content = ['01/08/01=01:00',
                       '01/08/01=01:00',
                       '01/08/01=03:00',
                       '01/09/01=00:00',
                       '01/10/01=00:00',
                       '01/11/01=00:00',
                       '-- Total=00:00',
                       '- Week 1:',
                       '-- Total=00:00',
                       '01/07/01=00:00',
                       '01/06/01=00:00',
                       '01/05/01=00:00',
                       '01/04/01=00:00',
                       '01/03/01=00:00',
                       '01/02/01=00:00',
                       '01/01/01=00:00',
                       '- Week 0:',
                       '12/25/00=00:00',
                       'nonsense...',
                       ':)']

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

        result = parse_log(log_content)
        expected = [Week(1, week1), Week(2, week2), Week(3, week3)]
        msg = 'Logs should be parsed and organized into weeks.'
        self.assertEqual(result, expected, msg)


    def test_log_data_total(self):
        log_content = ['04/01/22=10:15',
                       '04/02/22=01:00',
                       '04/08/22=06:15',
                       '04/10/22=03:05']

        result = LogData(log_content).total
        expected = hmt(20, 35)
        msg = 'LogData should calculate a grand total.'
        self.assertEqual(result, expected, msg)


if __name__ == '__main__':
    unittest.main()
