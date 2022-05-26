"""Error handling utilities."""

from enum import Enum
from typing import Callable, Optional


class Error(Enum):
    """An error containing a context dependant message."""

    PERMISSION = 'Need permission to access {} file.'
    NOT_FOUND = '{} file was not found.'
    PROFILE = '{} profile is invalid.'


def zip_error(callback: Callable, *args) -> (Optional[str], Optional[Error]):
    """Zip the output of a callback and an exception if one is raised."""

    output = None
    error = None

    try:
        output = callback(*args)

    except PermissionError:
        error = Error.PERMISSION

    except FileNotFoundError:
        error = Error.NOT_FOUND

    return (output, error)


def format_error(error: Error, context: str) -> str:
    """Apply a context to an error to create an error message."""

    return error.value.format(context).capitalize()
