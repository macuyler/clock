"""A log line representing a single day.

* Example day line:
04/20/22=05:43
"""

import datetime
from typing import Optional

from src.parse import parse
from src.time import Time, hmt

DATE_FORMAT = "%m/%d/%y"


class Day:

    def __init__(self, date: datetime.date, time: Time):
        self.date = date
        self.time = time


    def __str__(self):
        return f'{self.date.strftime(DATE_FORMAT)}={self.time}'


    def __lt__(self, other):
        return self.date < other.date


    def __eq__(self, other):
        return self.date == other.date and self.time == other.time


def str_to_day(string: str) -> Optional[Day]:
    """Attempt to convert a string into a Day object."""

    out = None

    day_format = "%M/%D/%Y=%h:%m"
    legacy_day_format = "%M/%D/%Y: %h:%mHR"

    values = parse(day_format, string)
    legacy_values = parse(legacy_day_format, string)

    if None not in values:
        month, day, year, hours, mins = values
        out = Day(datetime.date(2000 + year, month, day), hmt(hours, mins))

    elif None not in legacy_values:
        month, day, year, hours, mins = legacy_values
        out = Day(datetime.date(2000 + year, month, day), hmt(hours, mins))

    return out
