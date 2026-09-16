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
        (10, 4, [2, 2, 3, 3]),
        (3, 5, [0, 0, 1, 1, 1]),
    ],
)
def test_should_split_integer_into_expected_parts(
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
        (3, 5),
    ],
)
def test_should_return_requested_number_of_parts(
    value: int,
    number_of_parts: int,
) -> None:
    assert len(split_integer(value, number_of_parts)) == number_of_parts


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (8, 1),
        (6, 2),
        (17, 4),
        (32, 6),
        (10, 3),
        (3, 5),
    ],
)
def test_parts_should_sum_to_original_value(
    value: int,
    number_of_parts: int,
) -> None:
    assert sum(split_integer(value, number_of_parts)) == value


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (17, 4),
        (32, 6),
        (10, 3),
        (3, 5),
    ],
)
def test_parts_should_be_sorted(
    value: int,
    number_of_parts: int,
) -> None:
    result = split_integer(value, number_of_parts)

    assert result == sorted(result)


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (17, 4),
        (32, 6),
        (10, 3),
        (3, 5),
    ],
)
def test_difference_between_parts_should_not_exceed_one(
    value: int,
    number_of_parts: int,
) -> None:
    result = split_integer(value, number_of_parts)

    assert max(result) - min(result) <= 1
