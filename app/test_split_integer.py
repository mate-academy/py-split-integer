import pytest

from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value, number_of_parts, expected",
    [
        (8, 1, [8]),
        (6, 2, [3, 3]),
        (17, 4, [4, 4, 4, 5]),
        (32, 6, [5, 5, 5, 5, 6, 6]),
        (10, 3, [3, 3, 4]),
        (12, 4, [3, 3, 3, 3]),
        (1, 1, [1]),
        (1, 3, [0, 0, 1]),
        (5, 5, [1, 1, 1, 1, 1]),
        (2, 5, [0, 0, 0, 1, 1]),
    ],
)
def test_split_integer_returns_expected_result(
    value: int,
    number_of_parts: int,
    expected: list[int],
) -> None:
    assert split_integer(value, number_of_parts) == expected


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (8, 1),
        (6, 2),
        (17, 4),
        (32, 6),
        (10, 3),
        (1, 3),
        (2, 5),
        (100, 10),
    ],
)
def test_split_integer_returns_exact_number_of_parts(
    value: int,
    number_of_parts: int,
) -> None:
    result: list[int] = split_integer(value, number_of_parts)

    assert len(result) == number_of_parts


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (8, 1),
        (6, 2),
        (17, 4),
        (32, 6),
        (10, 3),
        (1, 3),
        (2, 5),
        (100, 10),
    ],
)
def test_split_integer_returns_integers(
    value: int,
    number_of_parts: int,
) -> None:
    result: list[int] = split_integer(value, number_of_parts)

    assert all(isinstance(part, int) for part in result)


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (8, 1),
        (6, 2),
        (17, 4),
        (32, 6),
        (10, 3),
        (1, 3),
        (2, 5),
        (100, 10),
    ],
)
def test_split_integer_preserves_sum(
    value: int,
    number_of_parts: int,
) -> None:
    result: list[int] = split_integer(value, number_of_parts)

    assert sum(result) == value


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (8, 1),
        (6, 2),
        (17, 4),
        (32, 6),
        (10, 3),
        (1, 3),
        (2, 5),
        (100, 10),
    ],
)
def test_split_integer_returns_sorted_array(
    value: int,
    number_of_parts: int,
) -> None:
    result: list[int] = split_integer(value, number_of_parts)

    assert result == sorted(result)


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (8, 1),
        (6, 2),
        (17, 4),
        (32, 6),
        (10, 3),
        (1, 3),
        (2, 5),
        (100, 10),
    ],
)
def test_split_integer_parts_differ_by_at_most_one(
    value: int,
    number_of_parts: int,
) -> None:
    result: list[int] = split_integer(value, number_of_parts)

    assert max(result) - min(result) <= 1
