"""A week's worth of log lines."""

from src.day import day, format_time


class Week:

    def __init__(self, week_num:int, days:list[str]):
        self.week_num = week_num
        self.days = list(map(day, days))


    @property
    def total(self):
        """Calculate the total number of hours logged."""

        return sum(map(lambda x: x.time, self.days))


    def __str__(self):
        header = f'- Week {self.week_num}:'
        days = list(map(str, self.days))
        footer = f'-- Total={format_time(self.total)}'
        return '\n'.join([header, *days, footer])
