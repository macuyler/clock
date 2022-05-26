"""Clock log file configuration.

The config file is located at ~/.config/clock/clock.conf

* Config Format:
profile:/Absolute/Path/to/file.txt

* Example Config:
work:/Users/user/Documents/work/hours.txt
school:/Users/user/Documents/school-hours.txt
_notify_me:60.0
"""

import os
from pathlib import Path
from typing import Optional

from src.file import File
from src.parse import parse

CONFIG_PATH = f'{Path.home()}/.config/clock/clock.conf'

class Config:

    def __init__(self, conf_path: str = CONFIG_PATH):
        self.path = Path(conf_path)
        self.profiles = {}
        self.notify_me = 0.0
        self._touch()
        self._load()
        self._validate()


    def profile(self, name: str) -> Optional[Path]:
        """Get the path for a given profile name."""

        path = None

        if name in self.profiles:
            path = Path(self.profiles[name])

        return path


    def _touch(self):
        """Create a new config file, if one doesn't exist."""

        if not self.path.parent.exists():
            os.makedirs(self.path.parent)

        self.path.touch()


    def _load(self):
        """Load all profiles from the config file."""

        delim = ':'

        data, error = File(self.path).read()
        if error is None:
            for line in data.split('\n'):
                if delim in line:
                    name, path = line.split(delim)
                    self.profiles[name] = path.strip()

                if '_notify_me' in line:
                    minutes, = parse('_notify_me:%f', line)
                    self.notify_me = minutes or 0.0


    def _validate(self):
        """Remove any profile with an invalid path."""

        for name, path in list(self.profiles.items()):
            if not Path(path).exists():
                del self.profiles[name]


    def legacy(self) -> Optional[Path]:
        """Attempt to parse a legacy (<= v1.1.0) config file."""

        legacy_path = None
        data, error = File(self.path).read()

        if error is None:
            path = Path(data.strip())
            if path.exists() and path.is_file():
                legacy_path = path

        return legacy_path
