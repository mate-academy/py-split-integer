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


def test_result_has_correct_length() -> None:
    result = split_integer(17, 4)

    assert len(result) == 4


def test_result_is_sorted() -> None:
    result = split_integer(17, 4)

    assert result == sorted(result)


def test_difference_between_max_and_min_is_not_greater_than_one() -> None:
    result = split_integer(17, 4)

    assert max(result) - min(result) <= 1


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (8, 1),
        (6, 2),
        (17, 4),
        (32, 6),
    ],
)
def test_sum_of_parts_equals_original_value(
    value: int,
    number_of_parts: int,
) -> None:
    assert sum(split_integer(value, number_of_parts)) == value
