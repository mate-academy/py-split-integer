import pytest
from app.split_integer import split_integer


# Test case to check if the result matches the expected output for one part
def test_single_part() -> None:
    result = split_integer(8, 1)
    assert result == [8]


# Test case to check if the result is correctly split into equal parts
def test_equal_parts() -> None:
    result = split_integer(6, 2)
    assert result == [3, 3]


# Test case to check if the result can handle more parts and is sorted
def test_multiple_parts() -> None:
    result = split_integer(17, 4)
    assert result == [4, 4, 4, 5]


# Test case to check if the result can handle more parts with some difference
def test_more_parts() -> None:
    result = split_integer(32, 6)
    assert result == [5, 5, 5, 5, 6, 6]


# Test case to check if the max-min difference is <= 1
def test_max_min_difference() -> None:
    result = split_integer(20, 5)
    max_min_diff = max(result) - min(result)
    assert max_min_diff <= 1


# Test case to check that the result is sorted in ascending order
def test_sorted_order() -> None:
    result = split_integer(50, 7)
    assert result == sorted(result)


# Test case to check if it handles case where parts are nearly equal
def test_nearly_equal_parts() -> None:
    result = split_integer(10, 3)
    assert result == [3, 3, 4]


# Test case to check edge case with large input
def test_large_input() -> None:
    result = split_integer(100, 20)
    assert result == [5] * 15 + [6] * 5


# Test case to check the behavior when the number is evenly divisible by parts
def test_divisible_by_parts() -> None:
    result = split_integer(12, 3)
    assert result == [4, 4, 4]
