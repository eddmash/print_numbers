import types

import pytest

from print_numbers.main import is_multiple, get_range_func


@pytest.mark.parametrize("n,x,expected", [
    (10, 5, True),
    (9, 5, False),
    (9, 3, True),
    (5, 3, False),
])

def test_is_multiple(n, x, expected):
    """test value is multiple"""
    assert is_multiple(n, x) == expected


def test_range_func_returns_generator():
    """check we get a generator object from range function"""
    range_func = get_range_func()

    isinstance(range_func(1,2), types.GeneratorType)

