"""A time tracking and logging utility."""

from datetime import datetime
from typing import Optional

from src.config import Config
from src.day import Day
from src.log import Log
from src.time import delta_to_time
from src.tools import IO, UI


class Clock:

    def __init__(self, profile: Optional[str] = None):
        self.profile = profile
        self.config = Config()
        self.start_time = None
        self.stop_time = None


    def start(self):
        self.start_time = datetime.now()


    def stop(self):
        self.stop_time = datetime.now()


    def run(self):
        """Run the time tracker."""

        self.start()

        value = ''
        while value != 'q' and self.start_time:
            UI.help()

            if value == 't':
                UI.show(datetime.now() - self.start_time)

            value = UI.input()

        self.stop()
        IO.log('Finished running clock.')


    def save(self):
        """Save clocked time to a log file."""

        if self.start_time and self.stop_time:
            date = self.start_time.date()
            time = delta_to_time(self.stop_time - self.start_time)
            clocked = Day(date, time)

            log_path = self.config.profile(self.profile)
            if log_path:
                log = Log(log_path)
                log.add(clocked)
                error = log.save()

            UI.save(clocked, error)

        self.start_time = None
        self.stop_time = None
