import pytest

from app.split_integer import split_integer


def test_sum_or_the_parts_should_be_equal_to_value():
    assert sum(split_integer(45, 4)) == 45


def test_should_split_into_equal_parts_when_value_is_divisible_by_parts():
    splited_integer = split_integer(25, 5)
    assert all(i == 5 for i in splited_integer)


def test_should_return_part_equals_to_a_value_when_slitting_into_one_part():
    assert split_integer(10, 1) == [10]


def test_parts_should_be_sorted_when_they_are_not_equal():
    splited_integer = split_integer(24, 5)
    splited_integer.sort()
    assert split_integer(24, 5) == splited_integer


def test_should_add_zeros_when_value_is_less_than_number_of_parts():
    assert split_integer(1, 5) == [1, 0, 0, 0, 0]
