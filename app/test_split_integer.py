import pytest
from app.split_integer import split_integer


@pytest.mark.parametrize("value, number_of_parts, expected", [
    (8, 1, [8]),
    (6, 2, [3, 3]),
    (17, 4, [4, 4, 4, 5]),
    (32, 6, [5, 5, 5, 5, 6, 6])
])
def test_sum_of_the_parts_should_be_equal_to_value(
        value,
        number_of_parts,
        expected
        ) -> None:
    assert split_integer(value, number_of_parts) == expected


@pytest.mark.parametrize("value, number_of_parts, expected",[
    (8, 1, [8]),
    (6, 2, [3, 3]),
    (18, 3, [6, 6, 6]),
    (30, 6, [5, 5, 5, 5, 5, 5])
])
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
        value,
        number_of_parts,
        expected) -> None:
    assert split_integer(value, number_of_parts) == expected


@pytest.mark.parametrize("value, number_of_parts, expected", [
    (8, 1, [8]),
    (6, 1, [6]),
    (18, 1, [18]),
    (30, 1, [30])
])
def test_should_return_part_equals_to_value_when_split_into_one_part(
        value,
        number_of_parts,
        expected) -> None:
    assert split_integer(value, number_of_parts) == expected


@pytest.mark.parametrize("value, number_of_parts, expected", [
    (17, 4, [4, 4, 4, 5]),
    (32, 6, [5, 5, 5, 5, 6, 6]),
])
def test_parts_should_be_sorted_when_they_are_not_equal(
        value,
        number_of_parts,
        expected) -> None:
    assert split_integer(value, number_of_parts) == expected


@pytest.mark.parametrize("value, number_of_parts, expected", [
    (3, 5, [0, 0, 1, 1, 1]),
    (2, 4, [0, 0, 1, 1]),
])
def test_should_add_zeros_when_value_is_less_than_number_of_parts(
        value,
        number_of_parts,
        expected) -> None:
    assert split_integer(value, number_of_parts) == expected
