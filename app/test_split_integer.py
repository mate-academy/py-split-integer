import pytest

from app.split_integer import split_integer


@pytest.mark.parametrize(
    "a,b,result",
    [
        (8, 2, 8),
        (1, 1, 1)
    ]
)
def test_sum_of_the_parts_should_be_equal_to_value(a: int, b: int, result: int) -> None:
    assert sum(split_integer(a, b)) == result


@pytest.mark.parametrize(
    "a,b,result",
    [
        (8, 2, [4, 4]),
        (1, 1, [1]),
        (6, 2, [3, 3])
    ]
)
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
        a: int,
        b: int,
        result: list[int]
) -> None:
    assert split_integer(a, b) == result


@pytest.mark.parametrize(
    "a,b,result",
    [
        (8, 1, [8]),
        (1, 1, [1]),
        (6, 1, [6])
    ]
)
def test_should_return_part_equals_to_value_when_split_into_one_part(
        a: int,
        b: int,
        result: list[int]
) -> None:
    assert split_integer(a, b) == result


@pytest.mark.parametrize(
    "a,b,result",
    [
        (7, 3, [2, 2, 3]),
        (20, 3, [6, 7, 7])
    ]
)
def test_parts_should_be_sorted_when_they_are_not_equal(
        a: int,
        b: int,
        result: list[int]
) -> None:
    assert split_integer(a, b) == result


@pytest.mark.parametrize(
    "a,b,result",
    [
        (2, 5, [0, 0, 0, 1, 1]),
        (3, 4, [0, 1, 1, 1]),
    ]
)
def test_should_add_zeros_when_value_is_less_than_number_of_parts(
        a: int,
        b: int,
        result: list[int]
) -> None:
    assert split_integer(a, b) == result