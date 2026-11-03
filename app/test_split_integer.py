import pytest

from app.split_integer import split_integer


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


def test_split_integer_returns_correct_number_of_parts() -> None:
    result = split_integer(17, 4)

    assert len(result) == 4


def test_split_integer_returns_sorted_list() -> None:
    result = split_integer(17, 4)

    assert result == sorted(result)


def test_split_integer_difference_between_max_and_min_not_more_than_one() -> None:
    result = split_integer(17, 4)

    assert max(result) - min(result) <= 1


def test_split_integer_sum_equals_original_value() -> None:
    result = split_integer(32, 6)

    assert sum(result) == 32
