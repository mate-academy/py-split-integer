import pytest
from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert(
        sum(split_integer(32, 6)) == 32
    ), f"Sum of {sum(split_integer(32, 6))} should be equal to {32}"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 12
    num_parts = 3
    parts = split_integer(value, num_parts)
    assert(
        all(part == value // num_parts for part in parts)
    ), "Each part should have the same value"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    parts = split_integer(2, 1)
    assert(
        parts[0] == 2
    ), f"Part should be equal value if {1} == 1"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    parts = split_integer(64, 7)
    assert(
        parts == sorted(parts)
    ), "Parts should be sorted"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    parts = split_integer(6, 10)
    assert(
        part == 0 for part in parts
    )
