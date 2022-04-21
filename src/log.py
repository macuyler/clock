"""A log of hours worked over a period of time.

* Example Log:
- Week 0:
01/01/01=00:00
01/02/01=00:00
01/03/01=00:00
01/04/01=00:00
01/05/01=00:00
01/06/01=00:00
01/07/01=00:00
-- Total=00:00

Grand Total = 00:00
"""

from pathlib import Path


class Log:

    def __init__(self, path:Path):
        self.path = path
        self.weeks = []
        self.total = 0.0
        self._load()

    def _load(self):
        """Load existing log data."""

        with self.path.open('r', encoding='utf-8') as log_file:
            lines = log_file.readlines()
            print(lines)
