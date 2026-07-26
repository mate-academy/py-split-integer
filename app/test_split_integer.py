import pytest
import app.split_integer as split_integer_module


@pytest.mark.parametrize("value, parts, expected", [
    (8, 1, [8]),
    (6, 2, [3, 3]),
    (17, 4, [4, 4, 4, 5]),
    (32, 6, [5, 5, 5, 5, 6, 6]),
])
def test_examples(value: int, parts: int, expected: list[int]) -> None:
    assert split_integer_module.split_integer(value, parts) == expected


@pytest.mark.parametrize("value, parts", [
    (1, 1),
    (6, 2),
    (17, 4),
    (32, 6),
    (2, 5),
    (10, 3),
    (10, 4),
    (100, 7),
])
def test_properties(value: int, parts: int) -> None:
    result = split_integer_module.split_integer(value, parts)
    assert len(result) == parts
    assert sum(result) == value
    assert result == sorted(result)
    assert result[-1] - result[0] <= 1


@pytest.mark.parametrize("value, parts", [
    (1, 1),
    (5, 2),
    (10, 3),
    (10, 4),
    (100, 7),
    (2, 5),
    (32, 6),
])
def test_matches_expected_distribution(value: int, parts: int) -> None:
    base = value // parts
    rem = value % parts
    expected = [base] * (parts - rem) + [base + 1] * rem
    assert split_integer_module.split_integer(value, parts) == expected


def test_when_value_less_than_parts_adds_zeros() -> None:
    result = split_integer_module.split_integer(2, 5)
    assert len(result) == 5
    assert sum(result) == 2
    assert result.count(1) == 2
    assert result[0] == 0
