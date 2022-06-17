import pytest
from app.split_integer import split_integer


def test_sum_or_the_parts_should_be_equal_to_value():
    assert sum(split_integer(32, 6)) == 32


def test_should_split_into_equal_parts_when_value_is_divisible_by_parts():
    assert split_integer(6, 2) == [3, 3]


def test_should_return_part_equals_to_a_value_when_slitting_into_one_part():
    assert split_integer(8, 1) == [8]


def test_parts_should_be_sorted_when_they_are_not_equal():
    assert split_integer(17, 4) == [4, 4, 4, 5]


def test_should_add_zeros_when_value_is_less_than_number_of_parts():
    assert split_integer(3, 4) == [0, 1, 1, 1]

