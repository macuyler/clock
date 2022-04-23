"""A week's worth of log lines."""

from functools import reduce
from operator import add
from typing import Union

from src.day import Day, str_to_day


class Week:

    def __init__(self, week_num:int, days:list[Union[str, Day]]):
        str_days = all(map(lambda d: isinstance(d, str), days))
        self.days = list(map(str_to_day, days)) if str_days else days
        self.week_num = week_num


    @property
    def total(self):
        return reduce(add, map(lambda x: x.time, self.days))


    def __str__(self):
        header = f'- Week {self.week_num}:'
        days = list(map(str, self.days))
        footer = f'-- Total={self.total}'
        return '\n'.join([header, *days, footer])


    def __eq__(self, other):
        return self.days == other.days
