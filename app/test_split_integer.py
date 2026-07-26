import pytest
from app.split_integer import split_integer


def test_sum_and_length_match() -> None:
    value, parts = 10, 3
    result = split_integer(value, parts)
    assert len(result) == parts
    assert sum(result) == value


def test_equal_parts_when_divisible() -> None:
    assert split_integer(6, 2) == [3, 3]
    assert split_integer(12, 4) == [3, 3, 3, 3]


def test_single_part_returns_value() -> None:
    assert split_integer(8, 1) == [8]


def test_sorted_and_balanced_when_not_equal() -> None:
    value, parts = 10, 3
    result = split_integer(value, parts)
    assert result == sorted(result)
    assert max(result) - min(result) <= 1
    assert sum(result) == value
    assert len(result) == parts


def test_add_zeros_when_value_less_than_parts() -> None:
    value, parts = 2, 5
    result = split_integer(value, parts)
    assert result == sorted(result)
    assert max(result) - min(result) <= 1
    assert sum(result) == value
    assert len(result) == parts


def test_matches_example_17_4() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5]


def test_matches_example_32_6() -> None:
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


@pytest.mark.parametrize("value,parts", [(10, 3), (11, 3), (5, 2), (2, 5)])
def test_max_min_diff_no_more_than_one(value: int, parts: int) -> None:
    result = split_integer(value, parts)
    assert len(result) == parts
    assert sum(result) == value
    assert result == sorted(result)
    assert max(result) - min(result) <= 1
