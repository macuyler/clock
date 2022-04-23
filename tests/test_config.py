"""Unit tests covering the src.config module."""

import os
import unittest
from pathlib import Path

from src.config import Config

from tests import cleanup, digits, setup


class TestConfig(unittest.TestCase):

    def test_touch_creates_path(self):
        """Test that __init__ creates missing directories in a path."""

        conf_path = f'{Path.home()}/.config/clock/{digits()}/{digits()}/conf'

        Config(conf_path)
        msg = 'All config file parent directories should be created.'
        self.assertTrue(os.path.exists(conf_path), msg)

        cleanup(conf_path)
        os.rmdir(Path(conf_path).parent)
        os.rmdir(Path(conf_path).parent.parent)


    def test_load_and_validate(self):
        """Test that __init__ loads and validates the config file."""

        conf_path = f'{Path.home()}/.config/clock/test.conf'
        log_path = f'{Path.home()}/hours.txt'

        test_profiles = [f'work:{log_path}',        # Valid Path
                         'school:/etc/shool.txt',   # Invalid Path
                         'alphabet_soup']           # Bad Format

        setup((conf_path, '\n'.join(test_profiles)),
              (log_path, None))

        conf = Config(conf_path)
        msg = 'Pofiles should be loaded from the config file and validated.'
        self.assertEqual(conf.profiles, {'work': log_path}, msg)

        cleanup(conf_path, log_path)


    def test_profiles(self):
        """Test that profiles can be queried."""

        conf_path = f'{Path.home()}/.config/clock/test.conf'
        log_path1 = f'{Path.home()}/hours1.txt'
        log_path2 = f'{Path.home()}/hours2.txt'

        test_profiles = [f'work:{log_path1}',
                         f'school:{log_path2}']


        setup((conf_path, '\n'.join(test_profiles)),
              (log_path1, None),
              (log_path2, None))

        conf = Config(conf_path)
        msg = 'You should be able to query config profiles.'
        self.assertEqual(conf.profile('work'), Path(log_path1), msg)
        self.assertEqual(conf.profile('school'), Path(log_path2), msg)
        msg = 'None should be returned for invalid profiles.'
        self.assertEqual(conf.profile(''), None, msg)

        cleanup(conf_path, log_path1, log_path2)


if __name__ == '__main__':
    unittest.main()
