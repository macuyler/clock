"""A log line representing a single day.

* Example day line:
04/20/22=05:43
"""

import datetime
import re
from typing import Optional

DATE_FORMAT = "%m/%d/%y"
LOG_FORMAT = re.compile(r'\d\d/\d\d/\d\d=\d\d:\d\d')

class Day:

    def __init__(self, date:datetime.date, time:float):
        self.date = date
        self.time = time


    def __str__(self):
        date_str = self.date.strftime(DATE_FORMAT)
        time_str = format_time(self.time)

        return f'{date_str}={time_str}'


def day(string:str) -> Optional[Day]:
    """Attempt to convert a string to a Day."""

    out = None
    string = string.strip()

    if LOG_FORMAT.match(string):
        date_str, time_str = string.split('=')
        hours, mins = time_str.split(':')
        time = float(hours) + float(mins) / 60
        date = datetime.datetime.strptime(date_str, DATE_FORMAT).date()
        out = Day(date, time)

    return out


def format_time(time:float):
    """Format decimal hours as a HR:MN string."""

    hours_str = str(int(time)).rjust(2, '0')
    mins_str = str(int(time * 100) % 100).rjust(2, '0')
    return f'{hours_str}:{mins_str}'
