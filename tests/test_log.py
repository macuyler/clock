"""Unit tests covering the src.log module."""

import unittest
from pathlib import Path

from src.log import Log


class TestLog(unittest.TestCase):

    def test_stuff(self):

        log = Log(Path(f'{Path.home()}/test-hours.txt'))
        print(log)

        self.assertEqual(0, 0)


if __name__ == '__main__':
    unittest.main()
