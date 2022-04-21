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
        hours_str = str(int(self.time)).rjust(2, '0')
        mins_str = str(int(self.time * 100) % 100)

        return f'{date_str}={hours_str}:{mins_str}'


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
