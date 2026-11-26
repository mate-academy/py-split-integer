import pytest

from app import split_integer


@pytest.mark.parametrize(
    "value, number_of_parts, expected",
    [
        (8, 1, [8]),
        (6, 2, [3, 3]),
        (17, 4, [4, 4, 4, 5]),
        (32, 6, [5, 5, 5, 5, 6, 6]),
        (10, 3, [3, 3, 4]),
        (11, 3, [3, 4, 4]),
        (5, 2, [2, 3]),
        (2, 4, [0, 0, 1, 1]),
        (1, 3, [0, 0, 1]),
    ]
)
def test_should_split_integer_into_expected_parts(
        value: int,
        number_of_parts: int,
        expected: list[int]
) -> None:
    assert (
        split_integer.split_integer(value, number_of_parts)
        == expected
    )


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (8, 1),
        (6, 2),
        (17, 4),
        (32, 6),
        (10, 3),
        (2, 4),
    ]
)
def test_should_return_only_integers(
        value: int,
        number_of_parts: int
) -> None:
    result = split_integer.split_integer(
        value,
        number_of_parts
    )

    assert all(type(part) is int for part in result)


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (17, 4),
        (32, 6),
        (10, 3),
        (11, 3),
        (2, 4),
    ]
)
def test_parts_should_be_sorted(
        value: int,
        number_of_parts: int
) -> None:
    result = split_integer.split_integer(
        value,
        number_of_parts
    )

    assert result == sorted(result)


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (17, 4),
        (32, 6),
        (10, 3),
        (11, 3),
        (2, 4),
    ]
)
def test_difference_between_min_and_max_should_not_exceed_one(
        value: int,
        number_of_parts: int
) -> None:
    result = split_integer.split_integer(
        value,
        number_of_parts
    )

    assert max(result) - min(result) <= 1


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (8, 1),
        (17, 4),
        (32, 6),
        (2, 4),
    ]
)
def test_should_return_exact_number_of_parts(
        value: int,
        number_of_parts: int
) -> None:
    result = split_integer.split_integer(
        value,
        number_of_parts
    )

    assert len(result) == number_of_parts


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (8, 1),
        (17, 4),
        (32, 6),
        (10, 3),
        (2, 4),
    ]
)
def test_should_preserve_total_value(
        value: int,
        number_of_parts: int
) -> None:
    result = split_integer.split_integer(
        value,
        number_of_parts
    )

    assert sum(result) == value
