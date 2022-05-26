"""A time based notification system."""

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
        if self.interval:
            self.timer.start()
            self.start_time = datetime.now()

    def stop(self):
        if self.timer.is_alive():
            self.timer.cancel()
            self.start_time = None

    def show(self):
        if self.start_time:
            content = UI.raw_show(datetime.now() - self.start_time)
            notification.notify(title="You are clocked in!", message=content)


# Ref: https://stackoverflow.com/questions/12435211/threading-timer-repeat-function-every-n-seconds
class RepeatTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)
