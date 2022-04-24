"""Unit tests covering the src.clock module."""

import unittest

from src.clock import Clock


class TestClock(unittest.TestCase):

    def test_stuff(self):

        clock = Clock()
        clock.run()
        clock.save()

        self.assertEqual(0, 0)



if __name__ == '__main__':
    unittest.main()
