"""A representaion of time as a number of minutes."""

import datetime


class Time:

    def __init__(self, value: int):
        self.value = value


    @property
    def hours(self) -> int:
        return int(self.value/60)


    @property
    def minutes(self) -> int:
        return self.value % 60


    def __str__(self):
        digits = lambda num: str(num).rjust(2, '0')
        return f'{digits(self.hours)}:{digits(self.minutes)}'


    def __add__(self, other):
        return Time(self.value + other.value)


    def __eq__(self, other):
        return self.value == other.value


def hmt(hours: int, minutes: int) -> Time:
    """Create a Time object from a number of hours and minutes."""

    return Time(hours * 60 + minutes)


def delta_to_time(delta: datetime.timedelta) -> Time:
    """Convert a timedelta into a Time object."""

    seconds = delta.total_seconds()
    minutes = round(seconds / 60)
    return Time(minutes)
