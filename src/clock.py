"""A time tracking and logging utility."""

from datetime import datetime
from typing import Optional

from src.config import Config
from src.day import Day
from src.error import Error
from src.log import Log
from src.notifier import Notifier
from src.time import delta_to_time
from src.tools import IO, UI


class Clock:

    def __init__(self, profile: Optional[str] = None, notify_me: Optional[float] = None):
        self.profile = profile
        self.config = Config()
        self.notifier = Notifier((notify_me or self.config.notify_me) * 60)
        self.start_time = None
        self.stop_time = None


    def start(self):
        self.notifier.start()
        self.start_time = datetime.now()


    def stop(self):
        self.notifier.stop()
        self.stop_time = datetime.now()
        IO.log('Finished running clock.')


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


    def save(self):
        """Save clocked time to a log file."""

        if self.start_time and self.stop_time:
            date = self.start_time.date()
            time = delta_to_time(self.stop_time - self.start_time)
            clocked = Day(date, time)

            error = None
            log_path = self.config.profile(self.profile)
            if log_path:
                log = Log(log_path)
                log.add(clocked)
                error = log.save()
            else:
                error = Error.PROFILE

            UI.save(clocked, error)

        self.start_time = None
        self.stop_time = None
