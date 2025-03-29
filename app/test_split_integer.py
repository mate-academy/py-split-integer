import pytest

from app.split_integer import split_integer


@pytest.mark.parametrize("value, number_of_parts", [
    (8, 1),
    (17, 4),
    (9, 3),
    (32, 6),
])
def test_sum_of_the_parts_should_be_equal_to_value(
    value: int, number_of_parts: int
) -> None:
    assert sum(split_integer(value, number_of_parts)) == value


@pytest.mark.parametrize("value, number_of_parts", [
    (6, 2),
    (9, 3),
    (12, 4),
])
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
    value: int, number_of_parts: int
) -> None:
    assert len(set(split_integer(value, number_of_parts))) == 1


@pytest.mark.parametrize("value", [
    9,
    17,
])
def test_should_return_part_equals_to_value_when_split_into_one_part(
    value: int
) -> None:
    assert split_integer(value, 1) == [value]


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (11, 2),
        (17, 3),
        (25, 4),
    ]
)
def test_parts_should_be_sorted_when_they_are_not_equal(
    value: int, number_of_parts: int
) -> None:
    assert split_integer(value, number_of_parts) == sorted(
        split_integer(value, number_of_parts)
    )


@pytest.mark.parametrize(
    "value, number_of_parts, expected",
    [
        (2, 5, [0, 0, 0, 1, 1]),
        (3, 4, [0, 1, 1, 1]),
        (0, 3, [0, 0, 0]),
    ]
)
def test_should_add_zeros_when_value_is_less_than_number_of_parts(
    value: int, number_of_parts: int, expected: list[int]
) -> None:
    assert split_integer(value, number_of_parts) == expected
