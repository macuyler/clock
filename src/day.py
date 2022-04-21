"""A log line representing a single day."""

import datetime


class Day:

    def __init__(self, date:datetime.date, time:float):
        self.date = date
        self.time = time
