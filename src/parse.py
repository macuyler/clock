"""A set of string parsing utilities."""

from collections import deque
from functools import reduce
from typing import Callable, Optional, Union

Parser = Callable[Optional[str], Optional[int]]
Pattern = list[Union[str, Parser]]

nop = lambda x: x


def compose(*func: Callable) -> Callable:
    """Compose a single function from the given set."""

    # Ref: https://www.geeksforgeeks.org/function-composition-in-python/
    merge = lambda f, g: lambda x: f(g(x))
    return reduce(merge, func, nop)


def check(condition: Callable[str, bool]) -> Parser:
    """Return None if the given condition fails."""

    return lambda x: x if x is None or condition(x) else None


def int_parser(minimum: Optional[int] = None, maximum: Optional[int] = None) -> Parser:
    """Create an integer parsing function with the given bounds."""

    apply_min = check(lambda x: x >= minimum)
    apply_max = check(lambda x: x <= maximum)

    return compose(apply_max if maximum else nop,
                   apply_min if minimum else nop,
                   int)


def get_pattern(fmt: str) -> Pattern:
    """Generate a pattern from the given format string."""

    flags = {
        'Y': int_parser(minimum=0, maximum=99),
        'M': int_parser(minimum=1, maximum=12),
        'D': int_parser(minimum=1, maximum=31),
        'h': int_parser(minimum=0),
        'm': int_parser(minimum=0, maximum=59),
    }

    output = []
    flagged = False
    delim = ''

    for char in fmt:

        if flagged and char in flags:
            output.append(flags[char])
            continue

        if char == '%':
            flagged = True

            if delim:
                output.append(delim)
                delim = ''

        else:
            delim += char

    if delim:
        output.append(delim)

    return output


def parse(pattern: Pattern, string: str) -> list[Optional[int]]:
    """Parse a set of integers from the given value according to a pattern."""

    prefix = pattern[0]
    if isinstance(prefix, str) and string.startswith(prefix):
        string = string[len(prefix):]
        pattern = pattern[1:]

    suffix = pattern[-1]
    if isinstance(suffix, str) and string.endswith(suffix):
        string = string[:len(string) - len(suffix)]
        pattern = pattern[:-1]

    output = []
    string = deque(string)

    handle = None
    delim = None

    for i, item in enumerate(pattern):
        if callable(item):
            handle = item
        elif isinstance(item, str):
            delim = item

        delim_check = ''
        value = ''

        if delim:
            while delim_check != delim and len(string) > 0:
                char = string.popleft()

                if delim.startswith(delim_check + char):
                    delim_check += char
                else:
                    value += char

            delim = None

        if delim is None and i == len(pattern) - 1:
            value = ''.join(string)

        if handle and value:
            try:
                output.append(handle(value))
            except ValueError:
                output.append(None)

    delim_count = len(list(filter(lambda x: isinstance(x, str), pattern)))
    while len(output) < delim_count + 1:
        output.append(None)

    return output
