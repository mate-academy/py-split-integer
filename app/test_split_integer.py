import pytest

from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (1, 1),
        (100, 19),
        (12, 11)

    ]
)
def test_sum_of_the_parts_should_be_equal_to_value(
        value: int,
        number_of_parts: int
) -> None:
    assert sum(split_integer(value, number_of_parts)) == value


@pytest.mark.parametrize(
    "value, number_of_parts, expected",
    [
        (20, 10, [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]),
        (60, 4, [15, 15, 15, 15]),
        (1000, 5, [200, 200, 200, 200, 200])
    ]
)
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
        value: int,
        number_of_parts: int,
        expected: list[int]
) -> None:
    assert split_integer(value, number_of_parts) == expected


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (17, 1),
        (9, 1),
        (1000, 1)

    ]
)
def test_should_return_part_equals_to_value_when_split_into_one_part(
        value: int,
        number_of_parts: int
) -> None:
    assert split_integer(value, number_of_parts) == [value]


@pytest.mark.parametrize(
    "value, number_of_parts, expected",
    [
        (20, 9, [2, 2, 2, 2, 2, 2, 2, 3, 3]),
        (4, 3, [1, 1, 2]),
        (
            1000,
            12,
            [83, 83, 83, 83, 83, 83, 83, 83, 84, 84, 84, 84]
        )
    ]
)
def test_parts_should_be_sorted_when_they_are_not_equal(
        value: int,
        number_of_parts: int,
        expected: list[int]
) -> None:
    assert split_integer(value, number_of_parts) == expected


@pytest.mark.parametrize(
    "value, number_of_parts, expected",
    [
        (
            20,
            21,
            [
                0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
            ]
        ),
        (0, 10, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
        (
            10,
            19,
            [
                0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
            ]
        )

    ]
)
def test_should_add_zeros_when_value_is_less_than_number_of_parts(
        value: int,
        number_of_parts: int,
        expected: list[int]
) -> None:
    assert split_integer(value, number_of_parts) == expected


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (17, 0),
        (9, 9),
        (1000, 1),
        (10, 11)
    ]
)
def test_should_return_array_with_exact_number_of_parts(
        value: int,
        number_of_parts: int
) -> None:
    assert len(split_integer(value, number_of_parts)) == number_of_parts


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (17, 3),
        (9, 4),
        (1000, 7)
    ]
)
def test_difference_between_parts_should_be_less_or_equal_than_1(
        value: int,
        number_of_parts: int
) -> None:
    result = split_integer(value, number_of_parts)
    assert max(result) - min(result) <= 1
