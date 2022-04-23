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
from pathlib import Path

from src.day import Day, str_to_day
from src.time import hmt
from src.week import Week


class Log:

    def __init__(self, path:Path):
        self.path = path
        self.weeks = []
        self.total = 0.0
        self._load()

    def _load(self):
        """Load and process existing log data."""

        with self.path.open('r', encoding='utf-8') as log_file:
            lines = log_file.readlines()

        is_day = lambda x: not x is None
        days = list(filter(is_day, map(str_to_day, lines)))
        days.sort()
        days = rectify(days)

        week_length = 7
        week_days = [ days[i:i+week_length] for i in range(0, len(days), week_length)]
        # Ref: https://www.geeksforgeeks.org/break-list-chunks-size-n-python/

        for i, week in enumerate(week_days):
            # Convert days back to string?
            week = list(map(str, week))

            self.weeks.append(Week(i + 1, week))


    def __str__(self):
        return '\n'.join(map(str, self.weeks))


def rectify(days:list[Day]) -> list[Day]:
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
            new_days += missing(day, next_day)
            carrier = hmt(0, 0)

        else:
            new_days.append(current)

    return new_days


def missing(start:Day, end:Day) -> list[Day]:
    """Create a list of all days between the given dates."""

    one_day = datetime.timedelta(days=1)
    gap = end.date - start.date
    missing_days = []

    while gap > one_day:
        gap -= one_day
        day = Day(end.date - gap, hmt(0, 0))
        missing_days.append(day)

    return missing_days
