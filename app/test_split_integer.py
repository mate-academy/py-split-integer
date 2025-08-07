import pytest
from app.split_integer import split_integer

def test_single_part():
    # Случай, когда number_of_parts == 1
    assert split_integer(8, 1) == [8]

def test_two_equal_parts():
    # Равномерное деление на две части
    assert split_integer(6, 2) == [3, 3]

def test_four_parts_with_remainder():
    # Деление с остатком, части отличаются не более чем на 1
    result = split_integer(17, 4)
    assert result == [4, 4, 4, 5]
    assert len(result) == 4
    assert max(result) - min(result) <= 1
    assert result == sorted(result)

def test_six_parts_with_remainder():
    result = split_integer(32, 6)
    assert result == [5, 5, 5, 5, 6, 6]
    assert len(result) == 6
    assert max(result) - min(result) <= 1
    assert result == sorted(result)

def test_large_value_and_parts():
    value = 1000
    parts = 33
    result = split_integer(value, parts)
    assert len(result) == parts
    assert max(result) - min(result) <= 1
    assert sum(result) == value
    assert result == sorted(result)

def test_minimal_parts():
    value = 1
    parts = 1
    assert split_integer(value, parts) == [1]

def test_value_equals_parts():
    value = 7
    parts = 7
    assert split_integer(value, parts) == [1, 1, 1, 1, 1, 1, 1]
