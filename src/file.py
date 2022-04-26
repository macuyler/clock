"""A generic read and write file handler."""

from pathlib import Path
from typing import Callable, Optional


class File:

    def __init__(self, path: Path, encoding: str = 'utf-8'):
        self.path = path
        self.encoding = encoding


    def read(self) -> (Optional[str], Optional[Exception]):
        """Attempt to read the content of the file and handle exceptions."""

        return zip_error(self._raw_read)


    def write(self, content: str) -> Optional[Exception]:
        """Attempt to write new content to the file and handle exceptions."""

        _, error = zip_error(self._raw_write, content)
        return error


    def _raw_read(self) -> str:
        """Read the content of the file."""

        with self.path.open('r', encoding=self.encoding) as file:
            return file.read()


    def _raw_write(self, content: str):
        """Write new content to the file."""

        with self.path.open('w', encoding=self.encoding) as file:
            file.write(content)


def zip_error(callback: Callable, *args) -> (Optional[str], Optional[Exception]):
    """Zip the output of a callback and an exception if one is raised."""

    output = None
    error = None

    try:
        output = callback(*args)

    except PermissionError:
        error = PermissionError

    except FileNotFoundError:
        error = FileNotFoundError

    return (output, error)
