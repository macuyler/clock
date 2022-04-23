"""A week's worth of log lines."""

from functools import reduce
from operator import add

from src.day import str_to_day


class Week:

    def __init__(self, week_num:int, days:list[str]):
        self.week_num = week_num
        self.days = list(map(str_to_day, days))


    @property
    def total(self):
        """Calculate the total amount of time logged."""

        return reduce(add, map(lambda x: x.time, self.days))


    def __str__(self):
        header = f'- Week {self.week_num}:'
        days = list(map(str, self.days))
        footer = f'-- Total={self.total}'
        return '\n'.join([header, *days, footer])
