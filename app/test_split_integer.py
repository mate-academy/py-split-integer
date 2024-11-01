import pytest
from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value,number_of_parts,result",
    [
        (8, 1, 8),
        (6, 2, 6),
        (17, 4, 17),
        (32, 6, 32)
    ]
)
def test_sum_of_the_parts_should_be_equal_to_value(
        value: int,
        number_of_parts: int,
        result: int
) -> None:
    assert (
        sum(split_integer(value, number_of_parts)) == result
    ), "Sum of the parts should be equal to value"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    result = split_integer(6, 2)
    assert (
        result[0] == result[1]
    ), "It should split into equal parts, when value is divisible by parts"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert (
        split_integer(8, 1)[0] == 8
    ), "It should return part equals to value, when split into one part"


@pytest.mark.parametrize(
    "value,number_of_parts,result",
    [
        (17, 4, [4, 4, 4, 5]),
        (32, 6, [5, 5, 5, 5, 6, 6])
    ]
)
def test_parts_should_be_sorted_when_they_are_not_equal(
        value: int,
        number_of_parts: int,
        result: list
) -> None:
    assert (
        split_integer(value, number_of_parts) == sorted(result)
    ), "Parts should be sorted, when they are not equal"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert (
        split_integer(1, 4) == [0, 0, 0, 1]
    ), "It should add zeros, when value is less than number of parts"
