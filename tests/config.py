"""Unit tests covering the src.config module."""

import os
import random
import unittest
from pathlib import Path

from src.config import Config


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


def setup(*files:(str, str)):
    """Setup test files."""

    for path, content in files:
        with open(path, 'w', encoding='utf-8') as file:
            file.write(content or '')


def cleanup(*files:str):
    """Remove test files."""

    for path in files:
        if os.path.exists(path):
            os.remove(path)


def digits():
    """Generate a random 4 digit number."""

    return str(random.randint(1111, 9999))


if __name__ == '__main__':
    unittest.main()
