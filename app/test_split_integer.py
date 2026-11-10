import pytest

from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (8, 1),
        (6, 2),
        (17, 4),
        (32, 6),
        (1, 3),
    ],
)
def test_sum_of_the_parts_should_be_equal_to_value(
        value: int,
        number_of_parts: int
) -> None:

    assert sum(split_integer(value, number_of_parts)) == value


@pytest.mark.parametrize(
    "value, number_of_parts, expected",
    [
        (6, 2, [3, 3]),
        (12, 3, [4, 4, 4]),
        (8, 1, [8]),
        (9, 9, [1] * 9)
    ],
)
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
        value: int,
        number_of_parts: int,
        expected: list
) -> None:
    assert split_integer(value, number_of_parts) == expected


@pytest.mark.parametrize(
    "value",
    [
        0,
        1,
        8,
        100,
    ],
)
def test_should_return_part_equals_to_value_when_split_into_one_part(
    value: int
) -> None:
    assert split_integer(value, 1) == [value]


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (17, 4),
        (8, 3),
        (7, 5),
        (32, 6),
    ],
)
def test_parts_should_be_sorted_when_they_are_not_equal(
        value: int,
        number_of_parts: int
) -> None:
    result = split_integer(value, number_of_parts)
    assert result == sorted(result)


@pytest.mark.parametrize(
    "value, number_of_parts, expected",
    [
        (1, 2, [0, 1]),
        (1, 3, [0, 0, 1]),
        (2, 5, [0, 0, 0, 1, 1]),
    ],
)
def test_should_add_zeros_when_value_is_less_than_number_of_parts(
        value: int,
        number_of_parts: int,
        expected: list
) -> None:
    assert split_integer(value, number_of_parts) == expected
