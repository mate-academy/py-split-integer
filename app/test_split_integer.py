# test_split_integer.py
from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 20
    number_of_parts = 6
    parts = split_integer(value, number_of_parts)
    assert (
        sum(parts) == value
    ), f"Sum of parts {parts} should be equal to {value}"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 10
    number_of_parts = 5
    parts = split_integer(value, number_of_parts)
    assert (
        parts == [2, 2, 2, 2, 2]
    ), (f"Parts should be equal when value {value} "
        f"is divisible by {number_of_parts}")


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 8
    number_of_parts = 1
    parts = split_integer(value, number_of_parts)
    assert (
        parts == [8]
    ), f"Should return [{value}] when number_of_parts is 1"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value = 17
    number_of_parts = 4
    parts = split_integer(value, number_of_parts)
    assert (
        parts == [4, 4, 4, 5]
    ), "Parts should be sorted in ascending order when they are not equal"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 3
    number_of_parts = 5
    parts = split_integer(value, number_of_parts)
    assert (
        parts == [0, 0, 1, 1, 1]
    ), ("Should return a list with zeros "
        "and ones when value is less than number_of_parts")
