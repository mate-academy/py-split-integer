import pytest
from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value, parts, expected",
    [
        (8, 1, [8]),
        (6, 2, [3, 3]),
        (17, 4, [4, 4, 4, 5]),
        (32, 6, [5, 5, 5, 5, 6, 6]),
        (3, 5, [0, 0, 1, 1, 1]),
    ],
    ids=[
        "single part equals value",
        "even split (divisible)",
        "uneven split (non-divisible)",
        "example from description",
        "more parts than value",
    ]
)
def test_split_integer_should_return_correct_parts_and_properties(
        value: int,
        parts: int,
        expected: list[int]
) -> None:
    result = split_integer(value, parts)
    assert result == expected
    assert len(result) == parts
    assert sum(result) == value
    assert result == sorted(result)
    assert max(result) - min(result) <= 1
    assert all(isinstance(x, int) for x in result)
