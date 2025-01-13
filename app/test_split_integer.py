import pytest
from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    result = split_integer(17, 4)
    assert sum(result) == 17, f"Expected sum to be 17, but got {sum(result)}"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    result = split_integer(12, 3)
    assert result == [4, 4, 4], f"Expected [4, 4, 4], but got {result}"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    result = split_integer(8, 1)
    assert result == [8], f"Expected [8], but got {result}"



def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer(17, 4)
    assert result == sorted(result), f"Expected sorted parts, but got {result}"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    result = split_integer(3, 5)
    assert result == [0, 0, 1, 1, 1], f"Expected [0, 0, 1, 1, 1], but got {result}"
