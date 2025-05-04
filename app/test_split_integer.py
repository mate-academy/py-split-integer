import pytest
from app.split_integer import split_integer

def test_single_part():
    assert split_integer(8, 1) == [8]

def test_even_split():
    assert split_integer(6, 2) == [3, 3]

def test_uneven_split():
    assert split_integer(17, 4) == [4, 4, 4, 5]

def test_larger_split():
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]

def test_parts_sorted_and_difference_valid():
    result = split_integer(100, 7)
    assert result == sorted(result)
    assert max(result) - min(result) <= 1
    assert len(result) == 7
    assert sum(result) == 100
