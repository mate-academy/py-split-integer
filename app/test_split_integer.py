"""Tests for split_integer function."""
from app.split_integer import split_integer


def test_sum_of_parts_equals_value() -> None:
    """Test that the sum of all parts equals the original value."""
    assert sum(split_integer(8, 1)) == 8
    assert sum(split_integer(6, 2)) == 6
    assert sum(split_integer(17, 4)) == 17
    assert sum(split_integer(32, 6)) == 32
    assert sum(split_integer(100, 7)) == 100


def test_returns_correct_number_of_parts() -> None:
    """Test that the result has exactly number_of_parts elements."""
    assert len(split_integer(8, 1)) == 1
    assert len(split_integer(6, 2)) == 2
    assert len(split_integer(17, 4)) == 4
    assert len(split_integer(32, 6)) == 6
    assert len(split_integer(100, 7)) == 7


def test_difference_between_min_and_max_is_at_most_one() -> None:
    """Test that max - min <= 1 for all results."""
    assert max(split_integer(17, 4)) - min(split_integer(17, 4)) <= 1
    assert max(split_integer(32, 6)) - min(split_integer(32, 6)) <= 1
    assert max(split_integer(10, 3)) - min(split_integer(10, 3)) <= 1
    assert max(split_integer(100, 7)) - min(split_integer(100, 7)) <= 1


def test_parts_are_sorted_ascending() -> None:
    """Test that the result is sorted in ascending order."""
    assert split_integer(10, 3) == [3, 3, 4]
    assert split_integer(17, 4) == [4, 4, 4, 5]
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]
    assert split_integer(20, 6) == [3, 3, 3, 3, 4, 4]
    assert split_integer(17, 5) == [3, 3, 3, 4, 4]


def test_split_into_one_part_returns_value() -> None:
    """Test that splitting into one part returns the original value."""
    assert split_integer(8, 1) == [8]
    assert split_integer(42, 1) == [42]
    assert split_integer(100, 1) == [100]


def test_split_evenly_divisible_values() -> None:
    """Test splitting values that are evenly divisible."""
    assert split_integer(6, 2) == [3, 3]
    assert split_integer(10, 2) == [5, 5]
    assert split_integer(12, 4) == [3, 3, 3, 3]
    assert split_integer(20, 4) == [5, 5, 5, 5]


def test_split_with_remainder() -> None:
    """Test splitting values with remainder."""
    assert split_integer(17, 4) == [4, 4, 4, 5]
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]
    assert split_integer(10, 3) == [3, 3, 4]
    assert split_integer(20, 6) == [3, 3, 3, 3, 4, 4]


def test_value_less_than_number_of_parts() -> None:
    """Test when value is less than number_of_parts (requires zeros)."""
    assert split_integer(1, 5) == [0, 0, 0, 0, 1]
    assert split_integer(3, 7) == [0, 0, 0, 0, 1, 1, 1]
    assert split_integer(2, 5) == [0, 0, 0, 1, 1]
    assert split_integer(5, 10) == [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]


def test_value_equals_number_of_parts() -> None:
    """Test when value equals number_of_parts."""
    assert split_integer(5, 5) == [1, 1, 1, 1, 1]
    assert split_integer(3, 3) == [1, 1, 1]
    assert split_integer(10, 10) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


def test_large_values() -> None:
    """Test with larger values."""
    assert len(split_integer(1000, 7)) == 7
    assert sum(split_integer(1000, 7)) == 1000
    assert max(split_integer(1000, 7)) - min(split_integer(1000, 7)) <= 1
    assert split_integer(1000, 7) == sorted(split_integer(1000, 7))

    assert len(split_integer(500, 13)) == 13
    assert sum(split_integer(500, 13)) == 500
    assert max(split_integer(500, 13)) - min(split_integer(500, 13)) <= 1
    assert split_integer(500, 13) == sorted(split_integer(500, 13))
