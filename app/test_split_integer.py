import pytest
from typing import List
from app.split_integer import split_integer

def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    test_cases = [
        (8, 1, [8]),
        (6, 2, [3, 3]),
        (17, 4, [4, 4, 4, 5]),
        (32, 6, [5, 5, 5, 5, 6, 6]),
    ]
    for value, number_of_parts, expected in test_cases:
        result = split_integer(value, number_of_parts)
        assert result == expected
        assert sum(result) == value

def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    test_cases = [
        (8, 4, [2, 2, 2, 2]),
        (10, 2, [5, 5]),
        (9, 3, [3, 3, 3]),
    ]
    for value, number_of_parts, expected in test_cases:
        assert split_integer(value, number_of_parts) == expected

def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    test_cases = [
        (8, 1, [8]),
        (5, 1, [5]),
        (15, 1, [15]),
    ]
    for value, number_of_parts, expected in test_cases:
        assert split_integer(value, number_of_parts) == expected

def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    test_cases = [
        (17, 4, [4, 4, 4, 5]),
        (32, 6, [5, 5, 5, 5, 6, 6]),
        (23, 5, [4, 4, 5, 5, 5]),
    ]
    for value, number_of_parts, expected in test_cases:
        result = split_integer(value, number_of_parts)
        assert result == sorted(result)

def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    test_cases = [
        (2, 5, [0, 0, 0, 1, 1]),
        (3, 7, [0, 0, 0, 0, 1, 1, 1]),
        (1, 4, [0, 0, 0, 1]),
    ]
    for value, number_of_parts, expected in test_cases:
        assert split_integer(value, number_of_parts) == expected

if __name__ == "__main__":
    pytest.main()
