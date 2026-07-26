import pytest
from app.split_integer import split_integer

def test_single_part():
    # Single part: output is just the value
    assert split_integer(8, 1) == [8]

def test_two_equal_parts():
    # Even split into two equal parts
    assert split_integer(6, 2) == [3, 3]

def test_four_parts_with_remainder():
    # Split with remainder, parts differ by at most 1
    assert split_integer(17, 4) == [4, 4, 4, 5]

def test_six_parts_with_remainder():
    # Split with remainder, parts differ by at most 1
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]

def test_large_value_and_parts():
    # Large value and parts; verify length, sum, order, and max-min difference
    value = 1000
    parts = 33
    result = split_integer(value, parts)
    assert len(result) == parts
    assert sum(result) == value
    assert max(result) - min(result) <= 1
    assert result == sorted(result)

def test_minimal_parts():
    # Minimal inputs: single part with value 1
    assert split_integer(1, 1) == [1]

def test_value_equals_parts():
    # Value equals number of parts: all ones
    assert split_integer(7, 7) == [1, 1, 1, 1, 1, 1, 1]
