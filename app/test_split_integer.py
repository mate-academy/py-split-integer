
from app import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer.split_integer(17, 4)) == 17


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer.split_integer(6, 2) == [3, 3]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer.split_integer(8, 1) == [8]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer.split_integer(17, 4) == [4, 4, 4, 5]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer.split_integer(3, 5) == [0, 0, 1, 1, 1]


def test_should_split_32_into_6_parts() -> None:
    assert split_integer.split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_should_split_11_into_4_parts() -> None:
    assert split_integer.split_integer(11, 4) == [2, 3, 3, 3]


def test_should_split_20_into_6_parts() -> None:
    assert split_integer.split_integer(20, 6) == [3, 3, 3, 3, 4, 4]


def test_should_split_14_into_4_parts() -> None:
    assert split_integer.split_integer(14, 4) == [3, 3, 4, 4]


def test_should_split_13_into_5_parts() -> None:
    assert split_integer.split_integer(13, 5) == [2, 2, 3, 3, 3]


def test_should_split_10_into_3_parts() -> None:
    assert split_integer.split_integer(10, 3) == [3, 3, 4]
