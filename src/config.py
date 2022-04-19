"""Clock log file configuration.

The config file is located at ~/.config/clock/clock.conf

Config Format:
profile:/Absolute/Path/to/file.txt

Example Config:
work:/Users/user/Documents/work/hours.txt
school:/Users/user/Documents/school-hours.txt
"""

import os
from pathlib import Path

CONFIG_PATH = f'{Path.home()}/.config/clock/clock.conf'

class Config:

    def __init__(self, conf_path: str=CONFIG_PATH):
        self.path = Path(conf_path)
        self.profiles = {}


    def touch(self):
        """Create a new config file, if one doesn't exist."""

        if not self.path.parent.exists():
            os.makedirs(self.path.parent)

        self.path.touch()


    def load(self):
        """Load all profiles from the config file."""

        delim = ':'

        with self.path.open('r', encoding='utf-8') as conf_file:
            lines = conf_file.readlines()

        for line in lines:
            if delim in line:
                name, path = line.split(delim)
                self.profiles[name] = path.strip()


    def validate(self):
        """Remove any profile with an invalid path."""

        invalid = []
        for name, path in self.profiles.items():
            if not Path(path).exists():
                invalid.append(name)

        for name in invalid:
            del self.profiles[name]


    def profile(self, name:str) -> Path:
        """Get the path for a given profile name."""

        path = list(self.profiles.values())[0]

        if name in self.profiles:
            path = self.profiles[name]

        return Path(path)
