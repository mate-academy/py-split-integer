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
def test_split_integer_returns_expected_parts_for_examples(
    value: int, number_of_parts: int, expected: list[int]
) -> None:
    assert split_integer(value, number_of_parts) == expected


def test_should_return_original_value_when_split_into_one_part() -> None:
    assert split_integer(9, 1) == [9]


def test_should_split_evenly_when_divisible() -> None:
    assert split_integer(12, 3) == [4, 4, 4]


def test_should_keep_parts_sorted_and_close_to_each_other() -> None:
    result = split_integer(25, 6)

    assert len(result) == 6
    assert result == sorted(result)
    assert max(result) - min(result) <= 1
    assert sum(result) == 25


def test_should_add_zeros_when_value_is_lower_than_parts() -> None:
    assert split_integer(3, 5) == [0, 0, 1, 1, 1]
