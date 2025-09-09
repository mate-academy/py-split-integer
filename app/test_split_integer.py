import pytest

from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value, number_of_parts, expected",
    [
        (8, 1, [8]),
        (6, 2, [3, 3]),
        (17, 4, [4, 4, 4, 5]),
        (32, 6, [5, 5, 5, 5, 6, 6]),
    ]
)
def test_sum_of_the_parts_should_be_equal_to_value(
        value: int,
        number_of_parts: int,
        expected: list
) -> None:
    assert split_integer(value, number_of_parts) == expected


@pytest.mark.parametrize(
    "value, number_of_parts, expected",
    [
        (8, 1, [8]),
        (6, 2, [3, 3]),
    ]
)
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
        value: int,
        number_of_parts: int,
        expected: list
) -> None:
    assert split_integer(value, number_of_parts) == expected


@pytest.mark.parametrize(
    "value, number_of_parts, expected",
    [
        (8, 1, [8]),
        (1, 1, [1]),
    ]
)
def test_should_return_part_equals_to_value_when_split_into_one_part(
        value: int,
        number_of_parts: int,
        expected: list
) -> None:
    assert split_integer(value, number_of_parts) == expected


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (17, 4),
        (7, 8),
        (32, 6),
    ]
)
def test_parts_should_be_sorted_when_they_are_not_equal(
        value: int,
        number_of_parts: int
) -> None:
    parts = split_integer(value, number_of_parts)
    assert parts == sorted(parts)


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (5, 6),
        (7, 8),
        (6, 32),
    ]
)
def test_should_add_zeros_when_value_is_less_than_number_of_parts(
        value: int,
        number_of_parts: int
) -> None:
    assert len(split_integer(value, number_of_parts)) == number_of_parts


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (8, 3),
        (10, 3),
        (100, 10)
    ]
)
def test_length_is_number_of_parts_for_value_ge_parts(
        value: int,
        number_of_parts: int
) -> None:
    assert len(split_integer(value, number_of_parts)) == number_of_parts


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (8, 3),
        (17, 4),
        (32, 6),
        (100, 9),
        (7, 8),
    ]
)
def test_difference_between_max_and_min_should_be_at_most_one(
        value: int,
        number_of_parts: int
) -> None:
    parts = split_integer(value, number_of_parts)
    assert max(parts) - min(parts) <= 1
