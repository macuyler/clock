"""A log line representing a single day.

* Example day line:
04/20/22=05:43
"""

import datetime
import re
from typing import Optional

from src.time import Time, str_to_time

DATE_FORMAT = "%m/%d/%y"
LOG_FORMAT = re.compile(r'\d\d/\d\d/\d\d=\d\d:\d\d')

class Day:

    def __init__(self, date:datetime.date, time:Time):
        self.date = date
        self.time = time


    def __str__(self):
        return f'{self.date.strftime(DATE_FORMAT)}={self.time}'


def str_to_day(string:str) -> Optional[Day]:
    """Attempt to convert a string into a Day object."""

    out = None
    string = string.strip()

    if LOG_FORMAT.match(string):
        date_str, time_str = string.split('=')
        date = datetime.datetime.strptime(date_str, DATE_FORMAT).date()
        time = str_to_time(time_str)
        out = Day(date, time)

    return out
