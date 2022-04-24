"""A log of hours worked over a period of time.

* Example Log:
- Week 0:
01/01/01=00:00
01/02/01=00:00
01/03/01=00:00
01/04/01=00:00
01/05/01=00:00
01/06/01=00:00
01/07/01=00:00
-- Total=00:00

Grand Total = 00:00
"""

import datetime
from functools import reduce
from operator import add
from pathlib import Path

from src.day import Day, str_to_day
from src.time import Time, hmt
from src.week import Week


class Log:
    """A log file handler."""

    def __init__(self, path: Path):
        self.path = path
        self.lines = []
        self._load()


    def _load(self):
        """Load existing log data."""

        with self.path.open('r', encoding='utf-8') as log_file:
            self.lines = log_file.readlines()


    def save(self):
        """Save current log data."""

        with self.path.open('w', encoding='utf-8') as log_file:
            log_file.write(LogData(self.lines))


class LogData:
    """Immutable log data represented as a list of Weeks."""

    def __init__(self, lines: list[str]):
        self._weeks = parse_log(lines)

    @property
    def weeks(self) -> list[Week]:
        return self._weeks


    @property
    def total(self) -> Time:
        return reduce(add, map(lambda x: x.total, self.weeks))


    def __str__(self):
        return '\n'.join(map(str, self.weeks)) + f'\n\nGrand Total = {self.total}'


def parse_log(lines: list[str]) -> list[Week]:
    """Parse lines from a log to generate a list of Weeks."""

    weeks = []

    is_day = lambda x: not x is None
    days = list(filter(is_day, map(str_to_day, lines)))
    days.sort()
    days = _rectify(days)

    week_length = 7
    raw_weeks = [days[i:i+week_length] for i in range(0, len(days), week_length)]
    # Ref: https://www.geeksforgeeks.org/break-list-chunks-size-n-python/

    for i, week_days in enumerate(raw_weeks):
        weeks.append(Week(i + 1, week_days))

    return weeks


def _rectify(days: list[Day]) -> list[Day]:
    """Combine duplicates and fill in missing days."""

    carrier = hmt(0, 0)
    new_days = []

    for i, day in enumerate(days):
        current = Day(day.date, day.time + carrier)

        if i < len(days) - 1:
            next_day = days[i + 1]

            if next_day.date == day.date:
                carrier += day.time
                continue

            new_days.append(current)
            new_days += _missing(day, next_day)
            carrier = hmt(0, 0)

        else:
            new_days.append(current)

    return new_days


def _missing(start: Day, end: Day) -> list[Day]:
    """Create a list of all days between the given dates."""

    one_day = datetime.timedelta(days=1)
    gap = end.date - start.date
    missing_days = []

    while gap > one_day:
        gap -= one_day
        day = Day(end.date - gap, hmt(0, 0))
        missing_days.append(day)

    return missing_days
