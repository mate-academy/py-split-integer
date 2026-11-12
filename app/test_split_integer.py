from __future__ import annotations

import pytest

from app.main import split_integer


def test_split_integer_into_one_part() -> None:
    assert split_integer(8, 1) == [8]


def test_split_integer_into_equal_parts() -> None:
    assert split_integer(6, 2) == [3, 3]


def test_split_integer_with_remainder() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5]


def test_split_integer_into_many_parts() -> None:
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_result_has_exact_number_of_parts() -> None:
    result = split_integer(17, 4)

    assert len(result) == 4


def test_result_is_sorted_ascending() -> None:
    result = split_integer(32, 6)

    assert result == sorted(result)


def test_difference_between_max_and_min_is_not_greater_than_one() -> None:
    result = split_integer(32, 6)

    assert max(result) - min(result) <= 1


def test_sum_of_parts_equals_original_value() -> None:
    result = split_integer(32, 6)

    assert sum(result) == 32


def test_all_parts_are_integers() -> None:
    result = split_integer(17, 4)

    assert all(isinstance(part, int) for part in result)


@pytest.mark.parametrize(
    "value, number_of_parts, expected",
    [
        (8, 1, [8]),
        (6, 2, [3, 3]),
        (17, 4, [4, 4, 4, 5]),
        (32, 6, [5, 5, 5, 5, 6, 6]),
    ],
)
def test_split_integer_returns_expected_result(
    value: int,
    number_of_parts: int,
    expected: list[int],
) -> None:
    assert split_integer(value, number_of_parts) == expected
