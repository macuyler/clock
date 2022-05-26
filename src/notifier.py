"""A time based notification system.

You can enable desktop notifications in your clock config file.
To receive notifications at a set interval, add a line with the
key `_notify_me` and a value of minutes in-between notifications.

* Example Config:
_notify_me:60.0
"""

from datetime import datetime
from threading import Timer
from typing import Optional

from plyer import notification

from src.tools import UI


class Notifier:

    def __init__(self, interval: Optional[float] = 0.0):
        self.interval = interval
        self.timer = RepeatTimer(interval, self.show)
        self.start_time = None


    def start(self):
        """Start the sending notifications at the set interval."""

        if self.interval:
            self.timer.start()
            self.start_time = datetime.now()


    def stop(self):
        """Stop sending notfications."""

        if self.timer.is_alive():
            self.timer.cancel()
            self.start_time = None


    def show(self):
        """Notify the user as to how long the clock has been running."""

        if self.start_time:
            content = UI.raw_show(datetime.now() - self.start_time)
            notification.notify(title="You are clocked in!", message=content)


# Ref: https://stackoverflow.com/questions/12435211/threading-timer-repeat-function-every-n-seconds
class RepeatTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)
