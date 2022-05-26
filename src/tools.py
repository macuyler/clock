"""A set of text based UI tools."""

import sys
from datetime import timedelta
from enum import Enum
from typing import Optional

from src.day import Day
from src.error import Error, format_error
from src.time import delta_to_time


class IOPrefix(Enum):
    INFO =  '[*]'
    ERROR = '[!]'


class IO:
    """Custom input/output utilities."""

    @staticmethod
    def print(*lines: str, prefix: IOPrefix = None):
        """Print lines to user over stderr."""

        for line in lines:
            out = f'{prefix.value} {line}' if prefix else line
            print(out, file=sys.stderr)


    @staticmethod
    def log(*lines: str):
        """Print lines with a [*] status prefix."""

        IO.print(*lines, prefix=IOPrefix.INFO)


    @staticmethod
    def error(*lines: str):
        """Print lines with a [!] error prefix."""

        IO.print(*lines, prefix=IOPrefix.ERROR)


    @staticmethod
    def list(title: str, items: list[str]):
        """Print a formatted list of items."""

        length = max(map(len, [title, *items])) + 2
        span = '━' * length

        top =    '┏' + span + '┓'
        middle = '┣' + span + '┫'
        bottom = '┗' + span + '┛'

        sides = lambda x: f'┃ {x}{" " * (length - len(x) - 2)} ┃'
        IO.print(top, sides(title), middle, *map(sides, items), bottom)


class UI:
    """An abstract user interface implementation."""

    @staticmethod
    def help():
        """Print a helpful list of options."""

        IO.list('You have clocked in...',
                ['Enter [t] to show time.',
                 'Enter [q] to quit.'])


    @staticmethod
    def input() -> str:
        """Read user input from stdin."""

        sys.stderr.write(' > ')
        return input()


    @staticmethod
    def show(delta: timedelta):
        """Show a time value to the user."""

        IO.print(UI.raw_show(delta))


    @staticmethod
    def raw_show(delta: timedelta):
        """Get a user friendly message showing time."""

        return f'Clocked in for {delta_to_time(delta)} so far.'


    @staticmethod
    def save(day: Day, error: Optional[Error]):
        """Alert the user to the state of their save data."""

        if error:
            IO.error('Failed to save data to the log file.')
            IO.error(format_error(error, 'the log'))

            IO.print('',
                     'Here is the time you just clocked for:',
                     '')
            print(day)
            IO.print('',
                     ' > You can save this to a clock log file.',
                     '   See the README for more details.')
        else:
            IO.log('Successfully saved data to the log file.')
