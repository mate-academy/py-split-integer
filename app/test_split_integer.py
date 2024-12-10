# app/test_split_integer.py

import pytest
from app.split_integer import split_integer  # Adjust based on your project structure

# Test case for a single part
def test_single_part():
    assert split_integer(8, 1) == [8]

# Test case for even split with 2 parts
def test_even_split_2_parts():
    assert split_integer(6, 2) == [3, 3]

# Test case for splitting into 4 parts with a non-even division
def test_non_even_split():
    assert split_integer(17, 4) == [4, 4, 4, 5]

# Test case for splitting into 6 parts with non-even division
def test_non_even_split_6_parts():
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]

# Test case for another non-even split with larger values
def test_large_non_even_split():
    assert split_integer(100, 8) == [12, 12, 12, 12, 12, 12, 13, 13]

# Test case for a split where the number is exactly divisible
def test_exact_division():
    assert split_integer(10, 2) == [5, 5]

# Test case for large numbers and a small number of parts
def test_large_numbers_small_parts():
    assert split_integer(1000, 2) == [500, 500]

# Test case for smallest number of parts greater than 1
def test_two_parts():
    assert split_integer(9, 2) == [4, 5]

# Test case where number is very small compared to the number of parts
def test_small_number_parts():
    assert split_integer(3, 3) == [1, 1, 1]

# Check if result array is sorted ascending (this is an implicit test of sorting behavior)
def test_sorted_order():
    result = split_integer(50, 7)
    assert result == sorted(result)

# Test for ensuring the max-min difference is <= 1
def test_max_min_difference():
    result = split_integer(20, 5)
    assert max(result) - min(result) <= 1
