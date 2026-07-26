# app/test_split_integer.py
import pytest
from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value, parts, expected",
    [
        (8, 1, [8]),
        (6, 2, [3, 3]),
        (10, 3, [3, 3, 4]),
        (17, 4, [4, 4, 4, 5]),
        (32, 6, [5, 5, 5, 5, 6, 6]),
        (23, 7, [3, 3, 3, 3, 3, 4, 4]),
        (29, 8, [3, 3, 3, 4, 4, 4, 4, 4]),
    ],
)
def test_expected_values(value: int, parts: int, expected: list[int]) -> None:
    """Test known correct outputs for given inputs."""
    assert split_integer(value, parts) == expected


@pytest.mark.parametrize("value, parts", [(10, 3), (23, 7), (32, 6)])
def test_sum_equals_value(value: int, parts: int) -> None:
    """Sum of parts must equal the original value."""
    assert sum(split_integer(value, parts)) == value


@pytest.mark.parametrize("value, parts", [(10, 3), (23, 7), (32, 6)])
def test_parts_count(value: int, parts: int) -> None:
    """Returned list must contain exactly 'parts' elements."""
    assert len(split_integer(value, parts)) == parts


@pytest.mark.parametrize("value, parts", [(10, 3), (23, 7), (32, 6)])
def test_sorted_and_difference(value: int, parts: int) -> None:
    """Result must be sorted ascending and max-min difference ≤ 1."""
    result = split_integer(value, parts)
    assert result == sorted(result)
    assert max(result) - min(result) <= 1
