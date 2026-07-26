import pytest
from app import split_integer


@pytest.mark.parametrize(
    "num1,num2",
    [
        (8, 2),
        (6, 4),
        (17, 4),
        (32, 6),
    ],
)
def test_diff_between_max_and_min_number_should_be_equal_or_minus_than_one(
    num1: int,
    num2: int,
) -> None:
    assert (
        max(split_integer.split_integer(num1, num2))
        - min(split_integer.split_integer(num1, num2))
        <= 1
    ), "the difference between the max and min"
    " number in the array should be <= 1;"


@pytest.mark.parametrize(
    "num1,num2",
    [
        (8, 2),
        (6, 4),
        (17, 4),
        (32, 6),
    ],
)
def the_array_should_be_sorted_ascending(
    num1: int,
    num2: int,
) -> None:
    assert split_integer.split_integer(num1, num2) == sorted(
        split_integer.split_integer(num1, num2)
    ), "the difference between the max and min"
    " number in the array should be <= 1;"


@pytest.mark.parametrize(
    "num1,num2",
    [
        (8, 1),
        (6, 2),
        (17, 4),
        (32, 6),
    ],
)
def test_sum_of_the_parts_should_be_equal_to_value(
    num1: int,
    num2: int,
) -> None:
    assert (
        sum(split_integer.split_integer(num1, num2)) == num1
    ), f"Sum of the split list from {num1} and {num2}"
    f"should be equal to {num1}"


@pytest.mark.parametrize(
    "num1,num2,result",
    [
        (8, 1, 8),
        (6, 2, 3),
        (16, 4, 4),
        (30, 6, 5),
    ],
)
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
    num1: int,
    num2: int,
    result: int,
) -> None:
    assert (
        split_integer.split_integer(num1, num2) == [result] * num2
    ), f"All the numbers of split list from {num1} and {num2}"
    f"should be equal to {result}"


@pytest.mark.parametrize(
    "num1,num2",
    [
        (8, 1),
        (6, 1),
        (16, 1),
        (12, 1),
    ],
)
def test_should_return_part_equals_to_value_when_split_into_one_part(
    num1: int,
    num2: int,
) -> None:
    assert split_integer.split_integer(num1, num2) == [
        num1
    ], f"Returned list from split list from {num1} and {num2}"
    f"should be a one elemnt list value {num1}"


@pytest.mark.parametrize(
    "num1,num2,result",
    [
        (17, 4, [4, 4, 4, 5]),
        (32, 6, [5, 5, 5, 5, 6, 6]),
        (43, 4, [10, 11, 11, 11]),
    ],
)
def test_parts_should_be_sorted_when_they_are_not_equal(
    num1: int,
    num2: int,
    result: list,
) -> None:
    assert (
        split_integer.split_integer(num1, num2) == result
    ), f"Returnd list {result} should be sorted"


@pytest.mark.parametrize(
    "num1,num2,result",
    [
        (4, 5, [0, 1, 1, 1, 1]),
        (2, 5, [0, 0, 0, 1, 1]),
        (7, 12, [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]),
    ],
)
def test_should_add_zeros_when_value_is_less_than_number_of_parts(
    num1: int,
    num2: int,
    result: list,
) -> None:
    assert (
        split_integer.split_integer(num1, num2) == result
    ), "Functions should return zeros when "
    "value is less than number of parts"
