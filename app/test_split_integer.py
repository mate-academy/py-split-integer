"""Student tests for split_integer."""

from typing import List
from app.split_integer import split_integer


def test_single_part() -> None:
    assert split_integer(8, 1) == [8]


def test_equal_split() -> None:
    assert split_integer(6, 2) == [3, 3]


def test_with_remainder() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5]


def test_larger_split() -> None:
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_properties_many_values() -> None:
    # sanity sweep: sums, length, range(max-min)<=1, ascending
    for value in range(1, 51):
        for parts in range(1, value + 1):
            result: List[int] = split_integer(value, parts)
            assert len(result) == parts
            assert sum(result) == value
            assert max(result) - min(result) <= 1
            assert result == sorted(result)
