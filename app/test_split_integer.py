import pytest
from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (8, 1),
        (17, 4),
        (-32, 6)
    ]
)
def test_sum_of_the_parts_should_be_equal_to_value(
        value: int,
        number_of_parts: int,
) -> None:
    assert (
        sum(split_integer(value, number_of_parts)) == value
    ), "Sum of parts not equal to value"


@pytest.mark.parametrize(
    "value, num_of_parts",
    [
        (6, 2),
        (-27, 3)
    ]
)
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
        value: int,
        num_of_parts: int
) -> None:
    assert (
        len(set(split_integer(value, num_of_parts))) == 1
    ), "Result should contain equal parts"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert (
        split_integer(100, 1) == [100]
    ), "Result should be equal to value"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer(32, 6)
    assert (
        result == sorted(result)
    ), "Result is not sorted"


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (1, 3),
        (100, 200)
    ]
)
def test_should_add_zeros_when_value_is_less_than_number_of_parts(
        value: int,
        number_of_parts: int
) -> None:
    result = split_integer(value, number_of_parts)
    number_of_zero = number_of_parts - value
    assert (
        result[:number_of_zero + 1].count(0) == number_of_zero
    ), "Function amount of zero is incorrect"
