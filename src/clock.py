"""A time tracking and logging utility."""

from datetime import datetime
from typing import Optional

from src.config import Config


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
        while value != 'q':
            value = input('> ')
        self.stop()
        print(self.stop_time - self.start_time)
