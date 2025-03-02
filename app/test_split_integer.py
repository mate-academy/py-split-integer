# app/test_split_integer.py
import pytest
from app.split_integer import split_integer

# Test that the sum of the parts equals the original value
def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    result = split_integer(17, 4)
    assert sum(result) == 17

# Test that the function splits into equal parts when the value is divisible by the number of parts
def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    result = split_integer(6, 2)
    assert result == [3, 3]

# Test that the result is just the value itself when splitting into one part
def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    result = split_integer(8, 1)
    assert result == [8]

# Test that the parts are sorted when they are not equal
def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer(17, 4)
    assert result == [4, 4, 4, 5]
    assert result == sorted(result)

# Test that the function correctly handles the case where value is less than number of parts
def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    result = split_integer(1, 5)
    assert result == [0, 0, 0, 0, 1]

# Additional test for handling different values and parts
def test_should_return_sorted_parts_with_difference_less_than_or_equal_to_1() -> None:
    result = split_integer(32, 6)
    assert result == [5, 5, 5, 5, 6, 6]
    # Verify that the difference between max and min is <= 1
    assert max(result) - min(result) <= 1
