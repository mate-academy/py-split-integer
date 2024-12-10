import pytest
from app.split_integer import split_integer

# Test case for a single part
def test_single_part() -> None:
    assert (split_integer
            (8, 1) ==
            [8])

# Test case for even split with 2 parts
def test_even_split_2_parts() -> None:
    assert (split_integer
            (6, 2) ==
            [3, 3])

# Test case for splitting into 4 parts with a non-even division
def test_non_even_split() -> None:
    assert (split_integer
            (17, 4) ==
            [4, 4, 4, 5])

# Test case for splitting into 6 parts with non-even division
def test_non_even_split_6_parts() -> None:
    assert (split_integer
            (32, 6) ==
            [5, 5, 5, 5, 6, 6])

# Test case for another non-even split with larger values
def test_large_non_even_split() -> None:
    assert (split_integer
            (100, 8) ==
            [12, 12, 12, 12, 12, 12, 13, 13])

# Test case for smallest number of parts greater than 1
def test_two_parts() -> None:
    assert (split_integer
            (9, 2) ==
            [4, 5])

# Test case where number is very small compared to the number of parts
def test_small_number_parts() -> None:
    assert (split_integer
            (3, 3) ==
            [1, 1, 1])

# Check if result array is sorted ascending (this is an implicit test of sorting behavior)
def test_sorted_order() -> None:
    result = split_integer(50, 7)
    assert result == sorted(result)

# Test for ensuring the max-min difference is <= 1
def test_max_min_difference() -> None:
    result = split_integer(20, 5)
    assert max(result) - min(result) <= 1
