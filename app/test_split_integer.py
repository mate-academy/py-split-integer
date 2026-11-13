import pytest

from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value, number_of_parts, expected",
    [
        (8, 1, [8]),
        (6, 2, [3, 3]),
        (17, 4, [4, 4, 4, 5]),
        (32, 6, [5, 5, 5, 5, 6, 6]),
        (1, 1, [1]),
        (1, 3, [0, 0, 1]),
        (3, 5, [0, 0, 1, 1, 1]),
        (10, 10, [1] * 10),
        (10, 3, [3, 3, 4]),
    ]
)
def test_split_integer_expected_result(
    value: int,
    number_of_parts: int,
    expected: list[int]
) -> None:
    assert split_integer(value, number_of_parts) == expected


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (1, 1),
        (10, 1),
        (10, 3),
        (20, 6),
        (3, 7),
        (100, 11),
    ]
)
def test_split_integer_returns_correct_number_of_parts(
    value: int,
    number_of_parts: int
) -> None:
    result = split_integer(value, number_of_parts)
    assert len(result) == number_of_parts


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (8, 1),
        (17, 4),
        (32, 6),
        (3, 5),
        (100, 9),
    ]
)
def test_split_integer_sum_equals_value(
    value: int,
    number_of_parts: int
) -> None:
    result = split_integer(value, number_of_parts)
    assert sum(result) == value


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (6, 2),
        (17, 4),
        (32, 6),
        (3, 5),
        (100, 7),
    ]
)
def test_split_integer_parts_differ_by_at_most_one(
    value: int,
    number_of_parts: int
) -> None:
    result = split_integer(value, number_of_parts)
    assert max(result) - min(result) <= 1


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (8, 1),
        (17, 4),
        (32, 6),
        (3, 5),
        (100, 9),
    ]
)
def test_split_integer_returns_sorted_parts(
    value: int,
    number_of_parts: int
) -> None:
    result = split_integer(value, number_of_parts)
    assert result == sorted(result)


def test_split_integer_returns_only_integers() -> None:
    result = split_integer(17, 4)
    assert all(isinstance(part, int) for part in result)
