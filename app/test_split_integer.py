import pytest

from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value, number_of_parts",
    [(8, 1), (6, 2), (17, 4), (32, 6)]
)
def test_sum_of_the_parts_should_be_equal_to_value(
    value: int,
    number_of_parts: int
) -> None:
    parts = split_integer(value, number_of_parts)
    assert sum(parts) == value


@pytest.mark.parametrize(
    "value, number_of_parts",
    [(8, 1), (6, 2), (12, 4), (100, 10)]
)
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
    value: int,
    number_of_parts: int
) -> None:
    expected_part = value // number_of_parts
    parts = split_integer(value, number_of_parts)
    assert all(part == expected_part for part in parts)


@pytest.mark.parametrize(
    "value, number_of_parts",
    [(1, 1), (8, 1), (100, 1)]
)
def test_should_return_part_equals_to_value_when_split_into_one_part(
    value: int,
    number_of_parts: int
) -> None:
    parts = split_integer(value, number_of_parts)
    assert parts == [value]


@pytest.mark.parametrize(
    "value, number_of_parts",
    [(8, 3), (6, 5), (17, 4), (32, 6)]
)
def test_parts_should_be_sorted_when_they_are_not_equal(
    value: int,
    number_of_parts: int
) -> None:
    parts = split_integer(value, number_of_parts)
    assert parts == sorted(parts)


@pytest.mark.parametrize(
    "value, number_of_parts",
    [(1, 5), (4, 5), (7, 30), (10, 100)]
)
def test_should_add_zeros_when_value_is_less_than_number_of_parts(
    value: int,
    number_of_parts: int
) -> None:
    parts = split_integer(value, number_of_parts)

    assert set(parts) <= {0, 1}
    assert parts.count(1) == value
    assert parts.count(0) == number_of_parts - value
    assert len(parts) == number_of_parts
