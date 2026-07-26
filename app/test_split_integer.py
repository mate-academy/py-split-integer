import pytest
from app.split_integer import split_integer


@pytest.mark.parametrize("value, number_of_parts", [
    (8, 1),
    (6, 2),
    (17, 4),
    (32, 6),
    (7, 3),
    (10, 10),
])
def test_sum_of_the_parts_should_be_equal_to_value(
    value: int,
    number_of_parts: int
) -> None:
    assert sum(split_integer(value, number_of_parts)) == value


@pytest.mark.parametrize("value, number_of_parts", [
    (8, 4),
    (6, 2),
    (15, 3),
])
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
    value: int,
    number_of_parts: int
) -> None:
    result = split_integer(value, number_of_parts)
    assert all(part == value // number_of_parts for part in result)


@pytest.mark.parametrize("value, number_of_parts", [
    (8, 1),
    (6, 1),
])
def test_should_return_part_equals_to_value_when_split_into_one_part(
    value: int,
    number_of_parts: int
) -> None:
    assert len(split_integer(value, number_of_parts)) == number_of_parts
    assert split_integer(value, number_of_parts)[0] == value


@pytest.mark.parametrize("value, number_of_parts", [
    (14, 3), (16, 5), (17, 4),
])
def test_parts_should_be_sorted_when_they_are_not_equal(
        value: int,
        number_of_parts: int) -> None:
    assert (
        split_integer(value, number_of_parts)
        == sorted(split_integer(value, number_of_parts))
    )


@pytest.mark.parametrize("value, number_of_parts, expected", [
    (4, 6, [0, 0, 1, 1, 1, 1]),
    (2, 3, [0, 1, 1]),
    (3, 5, [0, 0, 1, 1, 1]),
])
def test_should_add_zeros_when_value_is_less_than_number_of_parts(
        value: int,
        number_of_parts: int,
        expected: list
) -> None:
    assert split_integer(value, number_of_parts) == expected
