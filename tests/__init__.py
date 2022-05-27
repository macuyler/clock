"""Common unit test helper utilities."""

import os
import random


def setup(*files: (str, str)):
    """Setup test files."""

    for path, content in files:
        with open(path, 'w', encoding='utf-8') as file:
            file.write(content or '')


def cleanup(*files: str):
    """Remove test files."""

    for path in files:
        if os.path.exists(path):
            os.remove(path)


def digits() -> str:
    """Generate a random 4 digit number."""

    return str(random.randint(1111, 9999))
