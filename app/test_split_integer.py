import pytest

from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value,number_of_parts,expected",
    [
        (8, 1, [8]),
        (6, 2, [3, 3]),
        (17, 4, [4, 4, 4, 5]),
        (32, 6, [5, 5, 5, 5, 6, 6]),
    ],
)
def test_split_integer_result(
    value: int,
    number_of_parts: int,
    expected: list[int],
) -> None:
    assert split_integer(value, number_of_parts) == expected


@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        (8, 1),
        (6, 2),
        (17, 4),
        (32, 6),
        (10, 3),
        (100, 7),
    ],
)
def test_split_integer_number_of_parts(
    value: int,
    number_of_parts: int,
) -> None:
    result = split_integer(value, number_of_parts)

    assert len(result) == number_of_parts


@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        (8, 1),
        (6, 2),
        (17, 4),
        (32, 6),
        (10, 3),
        (100, 7),
    ],
)
def test_split_integer_sum(
    value: int,
    number_of_parts: int,
) -> None:
    result = split_integer(value, number_of_parts)

    assert sum(result) == value


@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        (8, 1),
        (6, 2),
        (17, 4),
        (32, 6),
        (10, 3),
        (100, 7),
    ],
)
def test_split_integer_difference(
    value: int,
    number_of_parts: int,
) -> None:
    result = split_integer(value, number_of_parts)

    assert max(result) - min(result) <= 1


@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        (8, 1),
        (6, 2),
        (17, 4),
        (32, 6),
        (10, 3),
        (100, 7),
    ],
)
def test_split_integer_sorted(
    value: int,
    number_of_parts: int,
) -> None:
    result = split_integer(value, number_of_parts)

    assert result == sorted(result)
