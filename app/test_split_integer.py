import pytest
from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value, parts, expected_result",
    [
        (8, 1, [8]),
        (6, 2, [3, 3]),
        (17, 4, [4, 4, 4, 5]),
        (32, 6, [5, 5, 5, 5, 6, 6]),
    ]
)
def test_split_integer(value: int, parts: int, expected_result: int) -> None:
    result = split_integer(value, parts)
    assert result == expected_result
    assert sum(result) == value


@pytest.mark.parametrize(
    "value, parts, expected_result",
    [
        (17, 4, [4, 4, 4, 5]),
    ]
)
def test_parts_should_be_sorted(
        value: int,
        parts: int,
        expected_result: int
) -> None:
    result = split_integer(value, parts)
    assert result == expected_result
    assert result == sorted(result)
