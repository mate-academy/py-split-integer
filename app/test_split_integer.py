from __future__ import annotations

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
def test_examples_and_common_cases(value: int, parts: int,
                                   expected: list[int]) -> None:
    assert split_integer(value, parts) == expected


@pytest.mark.parametrize(
    ("value", "parts"),
    [
        (1, 1),
        (1, 2),

        (3, 5),

        (9, 4),
        (17, 4),
        (32, 6),
        (50, 9),
    ],
)
def test_properties(value: int, parts: int) -> None:
    result: list[int] = split_integer(value, parts)

    assert len(result) == parts

    assert sum(result) == value

    assert result == sorted(result)

    if result:
        assert max(result) - min(result) <= 1

    assert all(isinstance(x, int) for x in result)
