"""An abstract user interface implementation."""

import sys
from datetime import timedelta

from src.day import Day
from src.time import delta_to_time


class Interface:

    @staticmethod
    def help():
        """Print a helpful list of options."""

        options = ['',
                   '',
                   '********************************',
                   '---- You have clocked in... ----',
                   ' * Enter [t] to show current time',
                   ' * Enter [q] to end',
                   '********************************',
                   '']

        print('\n'.join(options))


    @staticmethod
    def input() -> str:
        """Read user input from stdin."""

        prompt = '> '
        return input(prompt)


    @staticmethod
    def show(delta: timedelta):
        """Show a time value to the user."""

        print(f'Clocked for {delta_to_time(delta)} so far.\n')


    @staticmethod
    def save(day: Day):
        """Prompt the user to save their data via stdout."""

        prompt = ['',
                  '[*] Finished Running Clock.',
                  '[!] Could not find a log file.',
                  '',
                  'Here is the time you just clocked for:',
                  '']

        end_prompt = ['',
                      ' > You can save this to a clock log file.',
                      '   See the README for more details.']

        print('\n'.join(prompt), file=sys.stderr)
        print(day)
        print('\n'.join(end_prompt), file=sys.stderr)


    @staticmethod
    def saved():
        """Alert the user that their data was successfully saved."""

        prompt = ['',
                  '[*] Finished Running Clock.',
                  '[*] Saved data to log file.']

        print('\n'.join(prompt))
