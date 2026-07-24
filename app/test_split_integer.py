import pytest
from app import split_integer


def test_basic_case() -> None:
    assert split_integer.split_integer(8, 1) == [8]


def test_split_integer_6_2() -> None:
    assert split_integer.split_integer(6, 2) == [3, 3]


def test_split_on_equal_part() -> None:
    assert split_integer.split_integer(17, 4) == [4, 4, 4, 5]


def test_split_and_increment_the_last_number() -> None:
    assert split_integer.split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_split_on_incorrect_parts() -> None:
    assert split_integer.split_integer(8, 2) == [4, 4]
    assert split_integer.split_integer(10, 3) == [3, 3, 4]


def test_split_on_different_parts() -> None:
    assert split_integer.split_integer(2, 5) == [0, 0, 0, 1, 1]
    assert split_integer.split_integer(100, 10) == [10] * 10


@pytest.mark.parametrize(
    "value, number_of_parts, expected",
    [
        (10, 1, [10]),
        (8, 2, [4, 4]),
        (17, 4, [4, 4, 4, 5]),
        (32, 6, [5, 5, 5, 5, 6, 6]),
        (2, 5, [0, 0, 0, 1, 1]),
        (10, 3, [3, 3, 4]),
        (100, 10, [10] * 10),
    ]
)
def test_split_integer_exact(
    value: int,
    number_of_parts: int,
    expected: list
) -> None:
    assert split_integer.split_integer(value, number_of_parts) == expected


def test_sorted_ascending() -> None:
    assert (
        sorted(split_integer.split_integer(17, 4))
        == split_integer.split_integer(17, 4)
    )


def test_max_min_difference() -> None:
    assert (
        max(split_integer.split_integer(32, 6))
        - min(split_integer.split_integer(32, 6))
        <= 1
    )
