from typing import List
from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    pass


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    pass


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    pass


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    pass


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    pass


def test_single_part() -> None:
    assert split_integer(8, 1) == [8]


def test_equal_parts() -> None:
    assert split_integer(6, 2) == [3, 3]
    assert split_integer(12, 4) == [3, 3, 3, 3]


def test_with_remainder() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5]
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_boundary_conditions() -> None:
    assert split_integer(1, 1) == [1]
    assert split_integer(100, 10) == [10] * 10
    assert split_integer(101, 10) == [10] * 9 + [11]


def test_sorted_output() -> None:
    result: List[int] = split_integer(35, 5)
    assert result == sorted(result)


def test_difference_between_elements() -> None:
    result: List[int] = split_integer(17, 4)
    assert max(result) - min(result) <= 1


def test_sum_equals_value() -> None:
    value: int = 50
    number_of_parts: int = 7
    result: List[int] = split_integer(value, number_of_parts)
    assert sum(result) == value
    assert len(result) == number_of_parts
