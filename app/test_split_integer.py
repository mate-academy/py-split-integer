import pytest
from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    expected_result = [3, 3]
    value = 6
    number_of_parts = 2
    assert (expected_result, split_integer(value, number_of_parts)
            ), f"Sum of {number_of_parts} should be equal to {value}"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    expected_result = [5, 5, 5, 5, 6, 6]
    value = 32
    number_of_parts = 6
    assert (expected_result, split_integer(value, number_of_parts) and min(expected_result) != max(expected_result) or min(expected_result) + 1 != max(expected_result)
            ), f"Should split into equal parts"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    expected_result = [8]
    value = 8
    number_of_parts = 1
    assert (expected_result, split_integer(value, number_of_parts)
            ), f"if 'number_of_parts' equals_to {number_of_parts} should return {value}"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    expected_result = [4, 4, 4, 5]
    value = 17
    number_of_parts = 4
    assert (expected_result, split_integer(value, number_of_parts) and expected_result != sorted(expected_result)
            ), f"Parts should be sorted when they are not equal"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    expected_result = [1, 1, 1, 0]
    value = 3
    number_of_parts = 4
    assert (expected_result, split_integer(value, number_of_parts)
            ), f"Parts should be sorted when they are not equal"
