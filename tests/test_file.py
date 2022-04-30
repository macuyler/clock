"""Unit tests covering the src.file module."""

import os
import stat
import unittest
from pathlib import Path

from src.error import Error
from src.file import File

from tests import cleanup, setup


class TestFile(unittest.TestCase):

    def test_read_content(self):

        file_path = f'{Path.home()}/clock-test-read-file.txt'
        file_content = 'Hello World!'

        setup((file_path, file_content))

        result, error = File(Path(file_path)).read()
        expected_result = file_content
        expected_error = None
        result_msg = 'Result content should be read from the file.'
        error_msg = 'Error should be None after a successful read.'
        self.assertEqual(result, expected_result, result_msg)
        self.assertEqual(error, expected_error, error_msg)

        cleanup(file_path)


    def test_write_content(self):

        file_path = f'{Path.home()}/clock-test-write-file.txt'
        file_content = 'Why is the sky blue?'

        result = File(Path(file_path)).write(file_content)
        expected = None
        msg = 'None should be returned on successful write.'
        self.assertEqual(result, expected, msg)

        with open(file_path, 'r', encoding='utf-8') as test_file:
            result = test_file.read()

        expected = file_content
        msg = 'Content should be written to the file.'
        self.assertEqual(result, expected, msg)

        cleanup(file_path)


    def test_read_not_found_error(self):

        file_path = f'{Path.home()}/clock-test-read-error.txt'

        result, error = File(Path(file_path)).read()
        expected_result = None
        expected_error = FileNotFoundError
        expected_error = Error.NOT_FOUND
        result_msg = 'Result should be None after read error.'
        error_msg = 'Error should be FileNotFoundError when the file is missing.'
        self.assertEqual(result, expected_result, result_msg)
        self.assertEqual(error, expected_error, error_msg)


    def test_write_permission_error(self):

        file_path = f'{Path.home()}/clock-test-write-error.txt'
        file_content = "Can't touch this!"
        new_content = 'Nailed it.'

        setup((file_path, file_content))
        os.chmod(file_path, stat.S_IREAD)

        result = File(Path(file_path)).write(new_content)
        expected = PermissionError
        expected = Error.PERMISSION
        msg = 'PermissionError should be returned when writing to a protected file.'
        self.assertEqual(result, expected, msg)

        os.chmod(file_path, stat.S_IWRITE)
        cleanup(file_path)


if __name__ == '__main__':
    unittest.main()
