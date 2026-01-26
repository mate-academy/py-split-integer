import pytest

from app import split_integer


@pytest.mark.parametrize(
    "value, parts, expected",
    [
        (8, 1, [8]),
        (6, 2, [3, 3]),
        (17, 4, [4, 4, 4, 5]),
        (32, 6, [5, 5, 5, 5, 6, 6]),
        (3, 5, [0, 0, 1, 1, 1]),
        (8, 3, [2, 3, 3]),
    ],
)
def test_examples_and_edge_cases(
    value: int,
    parts: int,
    expected: list[int],
) -> None:
    assert split_integer.split_integer(value, parts) == expected


@pytest.mark.parametrize(
    "value, parts",
    [
        (1, 1),
        (2, 3),
        (8, 3),
        (10, 4),
        (25, 7),
        (100, 9),
    ],
)
def test_sum_of_parts_equals_value(value: int, parts: int) -> None:
    result = split_integer.split_integer(value, parts)
    assert sum(result) == value


@pytest.mark.parametrize(
    "value, parts",
    [
        (1, 1),
        (3, 5),
        (8, 3),
        (17, 4),
        (32, 6),
        (100, 9),
    ],
)
def test_result_has_required_length_and_is_sorted(
    value: int,
    parts: int,
) -> None:
    result = split_integer.split_integer(value, parts)
    assert len(result) == parts
    assert result == sorted(result)


@pytest.mark.parametrize(
    "value, parts",
    [
        (3, 5),
        (8, 3),
        (10, 4),
        (17, 4),
        (32, 6),
        (99, 10),
    ],
)
def test_max_minus_min_is_at_most_one(value: int, parts: int) -> None:
    result = split_integer.split_integer(value, parts)
    assert max(result) - min(result) <= 1


@pytest.mark.parametrize(
    "value, parts",
    [
        (8, 3),
        (11, 5),
        (14, 6),
        (3, 5),
    ],
)
def test_distribution_matches_floor_and_ceil_counts(
    value: int,
    parts: int,
) -> None:
    result = split_integer.split_integer(value, parts)

    floor_value = value // parts
    remainder = value % parts
    ceil_value = floor_value + (1 if remainder else 0)

    assert result.count(floor_value) == parts - remainder
    assert result.count(ceil_value) == remainder
