"""A time based notification system."""

from threading import Timer
from typing import Optional


class Notifier:

    def __init__(self, interval: Optional[float] = 0.0):
        self.interval = interval
        self.timer = RepeatTimer(interval, self.hit)
        self.running = False

    def start(self):
        if self.interval:
            self.timer.start()

    def stop(self):
        if self.timer.is_alive():
            self.timer.cancel()

    @staticmethod
    def hit():
        print("Hit!")


# Ref: https://stackoverflow.com/questions/12435211/threading-timer-repeat-function-every-n-seconds
class RepeatTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)
