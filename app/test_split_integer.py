import pytest
from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 25
    parts = 4
    result = split_integer(value, parts)
    assert sum(result) == value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 10
    parts = 5
    result = split_integer(value, parts)
    assert result == [2, 2, 2, 2, 2]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 7
    parts = 1
    result = split_integer(value, parts)
    assert result == [7]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value = 17
    parts = 3
    result = split_integer(value, parts)
    assert result == sorted(result)
    assert max(result) - min(result) <= 1


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 3
    parts = 5
    result = split_integer(value, parts)
    assert result == [0, 0, 1, 1, 1]
