"""A set of string parsing utilities."""

from collections import deque
from functools import reduce
from typing import Any, Callable, Optional, TypeVar, Union

nop = lambda x: x

Parser = Callable[Optional[str], Optional[TypeVar('T')]]
Pattern = list[Union[str, Parser]]


class ParsedValues:

    def __init__(self):
        self.values = []


    def __iter__(self):
        return iter(self.values)


    @property
    def success(self):
        return None not in self.values


    def append(self, value: Optional[int]):
        self.values.append(value)


    def try_to(self, parser: Optional[Parser], value: Optional[int]):
        """Attempt to parse an int from the given value."""

        if parser and value:
            try:
                self.append(parser(value))
            except ValueError:
                self.append(None)


    def fill_empty(self, pattern: Pattern):
        """Fill all empty values in the pattern with None."""

        values_wanted = len(list(filter(lambda x: isinstance(x, str), pattern))) + 1
        self.values += [None] * (values_wanted - len(self.values))


def cut(delim: str, string: deque) -> str:
    """Iterate through the given string until the delimiter is reached."""

    delim_check = ''
    value = ''

    if delim:
        while delim_check != delim and len(string) > 0:
            char = string.popleft()

            if delim.startswith(delim_check + char):
                delim_check += char
            else:
                value += char

    return value


def handle_affixes(pattern: Pattern, string: str) -> (Pattern, str):
    """Handle the prefix and suffix if present in the pattern."""

    prefix = pattern[0]
    if isinstance(prefix, str) and string.startswith(prefix):
        string = string[len(prefix):]
        pattern = pattern[1:]

    suffix = pattern[-1]
    if isinstance(suffix, str) and string.endswith(suffix):
        string = string[:len(string) - len(suffix)]
        pattern = pattern[:-1]

    return pattern, string


def parse(fmt: str, string: str) -> ParsedValues:
    """Parse a set of integers from the given value according to a pattern."""

    pattern, string = handle_affixes(get_pattern(fmt), string)
    output = ParsedValues()
    string = deque(string)
    handle = None
    delim = None

    for i, item in enumerate(pattern):
        handle = item if callable(item) else handle
        delim = item if isinstance(item, str) else delim

        value = cut(delim, string)
        delim = None

        if i == len(pattern) - 1 and not value:
            value = ''.join(string)

        output.try_to(handle, value)

    output.fill_empty(pattern)

    return output


def compose(*func: Callable) -> Callable:
    """Compose a single function from the given set."""

    # Ref: https://www.geeksforgeeks.org/function-composition-in-python/
    merge = lambda f, g: lambda *x: f(g(*x))
    return reduce(merge, func, nop)


def check(condition: Callable[str, bool]) -> Parser:
    """Return None if the given condition fails."""

    return lambda x: x if x is None or condition(x) else None


def bounds(parser: Parser[Any],
           minimum: Optional[Any] = None,
           maximum: Optional[Any] = None) -> Parser[Any]:
    """Add a min and max boundry to a string parser."""

    return compose(check(lambda x: x <= maximum) if maximum else nop,
                   check(lambda x: x >= minimum) if minimum else nop,
                   parser)


def get_pattern(fmt: str) -> Pattern:
    """Generate a pattern from the given format string."""

    flags = {
        'i': int,
        'f': float,
        'Y': bounds(int, minimum=0, maximum=99),
        'M': bounds(int, minimum=1, maximum=12),
        'D': bounds(int, minimum=1, maximum=31),
        'h': bounds(int, minimum=0),
        'm': bounds(int, minimum=0, maximum=59),
    }

    output = []
    flagged = False
    delim = ''

    for char in fmt:

        if flagged and char in flags:
            output.append(flags[char])
            flagged = False
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
