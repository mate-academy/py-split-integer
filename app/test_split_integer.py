import random

import pytest

from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    first_border = 1
    up_border = 5
    multiplayer = 100
    quant_of_parts = random.randint(first_border, up_border)
    for value in range(up_border, up_border * multiplayer,
                       random.randint(first_border, up_border)):
        result = split_integer(value, quant_of_parts)
        assert sum(result) == value, (f"sum of {quant_of_parts} parts:"
                                      f" {result} != value {value}")


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(9, 3) == [3, 3, 3]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(9, 1) == [9]


@pytest.mark.parametrize(
    "values, number, result", [
        (17, 4, [4, 4, 4, 5]),
        (32, 6, [5, 5, 5, 5, 6, 6])

    ]

)
def test_parts_should_be_sorted_when_they_are_not_equal(
        values: int,
        number: int,
        result: list
) -> None:
    assert split_integer(values, number) == result


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(8, 12).count(0) == 4
