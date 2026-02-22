import pytest
from app.split_integer import split_integer  # припускаємо, що функція в split_integer.py


def test_single_part():
    """Test splitting into 1 part returns original number"""
    result = split_integer(8, 1)
    assert result == [8]


def test_two_equal_parts():
    """Test splitting a number evenly into two parts"""
    result = split_integer(6, 2)
    assert result == [3, 3]


def test_split_with_remainder():
    """Test splitting with remainder distributes +1 to largest parts"""
    result = split_integer(17, 4)
    assert result == [4, 4, 4, 5]


def test_split_even_distribution():
    """Test splitting into parts where some numbers need to be +1"""
    result = split_integer(32, 6)
    assert result == [5, 5, 5, 5, 6, 6]


def test_length_matches_number_of_parts():
    """Ensure the returned array has exactly number_of_parts elements"""
    number, parts = 17, 4
    result = split_integer(number, parts)
    assert len(result) == parts


def test_difference_between_max_and_min():
    """Ensure the difference between max and min is <= 1"""
    number, parts = 17, 4
    result = split_integer(number, parts)
    assert max(result) - min(result) <= 1


def test_sorted_ascending():
    """Ensure the result array is sorted in ascending order"""
    number, parts = 17, 4
    result = split_integer(number, parts)
    assert result == sorted(result)