from app.split_integer import split_integer
import pytest


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 17
    result = sum(split_integer(value, 4))
    assert result == value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(100, 5) == [20, 20, 20, 20, 20]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(3, 5) == [0, 0, 1, 1, 1]


def test_should_return_zeros_when_value_is_zero():
    result = split_integer(0, 5)
    assert result == [0, 0, 0, 0, 0]


def test_should_raise_error_when_parts_is_zero():
    with pytest.raises(ValueError):
        split_integer(10, 0)