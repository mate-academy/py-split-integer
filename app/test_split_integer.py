"""Tests for split_integer function."""
import pytest
from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    """Test that the sum of all parts equals the original value."""
    assert sum(split_integer(10, 3)) == 10
    assert sum(split_integer(100, 7)) == 100
    assert sum(split_integer(50, 5)) == 50
    assert sum(split_integer(17, 5)) == 17


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:  # noqa: E501
    """Test splitting into equal parts when value is divisible."""
    assert split_integer(10, 2) == [5, 5]
    assert split_integer(12, 4) == [3, 3, 3, 3]
    assert split_integer(20, 4) == [5, 5, 5, 5]
    assert split_integer(18, 3) == [6, 6, 6]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:  # noqa: E501
    """Test that splitting into one part returns the original value."""
    assert split_integer(42, 1) == [42]
    assert split_integer(100, 1) == [100]
    assert split_integer(1, 1) == [1]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    """Test that parts are sorted in ascending order."""
    result = split_integer(10, 3)
    assert result == [3, 3, 4]
    assert result == sorted(result)

    result = split_integer(20, 6)
    assert result == [3, 3, 3, 3, 4, 4]
    assert result == sorted(result)

    result = split_integer(17, 5)
    assert result == sorted(result)

    # Verify max - min <= 1
    assert max(result) - min(result) <= 1


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:  # noqa: E501
    """Test that zeros are added when value is less than number of parts."""
    assert split_integer(1, 5) == [0, 0, 0, 0, 1]
    assert split_integer(3, 7) == [0, 0, 0, 0, 1, 1, 1]
    assert split_integer(5, 10) == [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

    # Verify all requirements still hold
    result = split_integer(2, 5)
    assert sum(result) == 2
    assert len(result) == 5
    assert result == sorted(result)
    assert max(result) - min(result) <= 1
