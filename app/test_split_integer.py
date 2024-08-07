import pytest

from app.split_integer import split_integer


def test_sum_of_parts_equals_value() -> None:
    assert sum(split_integer(17, 4)) == 17


@pytest.mark.parametrize(
    "value, parts_number, result",
    [
        (8, 2, [4, 4]),
        (9, 3, [3, 3, 3])
    ],
    ids=[
        "evens",
        "odds"
    ]
)
def test_parts_are_equal_if_value_divisible_by_number(
        value: int,
        parts_number: int,
        result: list
) -> None:
    assert split_integer(value, parts_number) == result


def test_returns_value_if_number_is_one() -> None:
    assert split_integer(8, 1) == [8]


def test_parts_are_sorted_when_they_are_not_equal() -> None:
    assert split_integer(17, 4) == sorted(split_integer(17, 4))


def test_add_zeros_when_value_is_less_than_number() -> None:
    assert split_integer(2, 4) == [0, 0, 1, 1]
