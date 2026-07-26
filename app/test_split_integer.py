import pytest
from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value_arg, number_of_parts_arg, result",
    [
        (2, 1, 2),
        (8, 1, 8),
        (17, 4, 17),
        (32, 6, 32)
    ]
)
def test_sum_of_the_parts_should_be_equal_to_value(
    value_arg: int,
    number_of_parts_arg: int,
    result: int
) -> None:
    assert sum(split_integer(value_arg, number_of_parts_arg)) == result


@pytest.mark.parametrize(
    "value_arg, number_of_parts_arg, result",
    [
        (8, 1, [8]),
        (6, 2, [3, 3]),
        (12, 3, [4, 4, 4]),
        (32, 4, [8, 8, 8, 8])
    ]
)
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
    value_arg: int,
    number_of_parts_arg: int,
    result: list
) -> None:
    assert split_integer(value_arg, number_of_parts_arg) == result


@pytest.mark.parametrize(
    "value_arg, number_of_parts_arg, result",
    [
        (8, 1, [8]),
        (6, 1, [6]),
        (12, 1, [12]),
        (32, 1, [32])
    ]
)
def test_should_return_part_equals_to_value_when_split_into_one_part(
    value_arg: int,
    number_of_parts_arg: int,
    result: list
) -> None:
    assert split_integer(value_arg, number_of_parts_arg) == result


@pytest.mark.parametrize(
    "value_arg, number_of_parts_arg, result",
    [
        (6, 4, [1, 1, 2, 2]),
        (12, 5, [2, 2, 2, 3, 3]),
        (32, 3, [10, 11, 11])
    ]
)
def test_parts_should_be_sorted_when_they_are_not_equal(
    value_arg: int,
    number_of_parts_arg: int,
    result: list
) -> None:
    assert split_integer(value_arg, number_of_parts_arg) == result


@pytest.mark.parametrize(
    "value_arg, number_of_parts_arg, result",
    [
        (1, 2, [0, 1]),
        (5, 8, [0, 0, 0, 1, 1, 1, 1, 1]),
        (4, 6, [0, 0, 1, 1, 1, 1])
    ]
)
def test_should_add_zeros_when_value_is_less_than_number_of_parts(
    value_arg: int,
    number_of_parts_arg: int,
    result: list
) -> None:
    assert split_integer(value_arg, number_of_parts_arg) == result


@pytest.mark.parametrize(
    "value_arg, number_of_parts_arg",
    [
        (6, 4),
        (12, 5),
        (32, 3)
    ]
)
def test_should_test_parts_should_be_sorted_in_ascending_order(
    value_arg: int,
    number_of_parts_arg: int,
) -> None:
    actual = split_integer(value_arg, number_of_parts_arg)
    assert actual == sorted(actual)


@pytest.mark.parametrize(
    "value_arg, number_of_parts_arg",
    [
        (8, 1),
        (6, 2),
        (12, 3),
        (32, 4),
        (6, 4),
        (12, 5),
        (32, 3)
    ]
)
def test_difference_between_min_and_max_should_be_not_exceed_1(
    value_arg: int,
    number_of_parts_arg: int
) -> None:
    actual = split_integer(value_arg, number_of_parts_arg)
    assert max(actual) - min(actual) <= 1
