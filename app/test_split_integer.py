import random

import pytest

from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    quant_of_parts = random.randint(2, 5)
    for value in range(5, 100, random.randint(1, 5)):
        result = split_integer(value, quant_of_parts)
        assert sum(result) == value, \
            f"sum of {quant_of_parts} parts: {result} != value {value}"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    result = split_integer(9, 3)
    assert set(result) == {3}


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
