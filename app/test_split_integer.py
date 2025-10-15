# app/test_split_integer.py
import pytest
from app.split_integer import split_integer


@pytest.mark.parametrize(
    ("value", "parts", "expected"),
    [
        (8, 1, [8]),
        (6, 2, [3, 3]),
        (17, 4, [4, 4, 4, 5]),
        (32, 6, [5, 5, 5, 5, 6, 6]),
        (10, 5, [2, 2, 2, 2, 2]),
        (7, 3, [2, 2, 3]),
        (5, 5, [1, 1, 1, 1, 1]),
    ],
)
def test_examples_and_common_cases(value: int,
                                   parts: int, expected: list[int]) -> None:
    assert split_integer(value, parts) == expected


@pytest.mark.parametrize(("value", "parts"), [(9, 4), (17, 4), (32, 6)])
def test_sorted_and_difference_leq_one(value: int, parts: int) -> None:
    result: list[int] = split_integer(value, parts)
    assert result == sorted(result)
    assert max(result) - min(result) <= 1


@pytest.mark.parametrize(("value", "parts"),
                         [(8, 1), (6, 2), (17, 4), (32, 6)])
def test_sum_equals_original_value(value: int, parts: int) -> None:
    result: list[int] = split_integer(value, parts)
    assert sum(result) == value
