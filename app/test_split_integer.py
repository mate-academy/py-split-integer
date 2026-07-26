import pytest
from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value, num_parts", [
        (8, 1),
        (6, 2),
        (17, 4),
        (32, 6)
    ]
)
def test_difference_between_max_and_min_should_be_less_than_or_equal_to_one(
    value: int,
    num_parts: int
) -> None:
    assert max(split_integer(value, num_parts)) - min(
        split_integer(value, num_parts)) <= 1


@pytest.mark.parametrize(
    "value, num_parts", [
        (8, 1),
        (6, 2),
        (17, 4),
        (32, 6)
    ]
)
def test_sum_of_the_parts_should_be_equal_to_value(
    value: int,
    num_parts: int
) -> None:
    assert sum(split_integer(value, num_parts)) == value


@pytest.mark.parametrize(
    "value, num_parts", [
        (7, 1),
        (49, 7),
        (100, 10),
        (8, 4)
    ]
)
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
    value: int,
    num_parts: int
) -> None:
    assert len(set(split_integer(value, num_parts))) == 1


@pytest.mark.parametrize(
    "value", [
        7,
        8,
        137,
        66
    ]
)
def test_should_return_part_equals_to_value_when_split_into_one_part(
    value: int
) -> None:
    assert split_integer(value, 1)[0] == value


@pytest.mark.parametrize(
    "value, num_parts", [
        (13, 3),
        (17, 4),
        (100, 10)
    ]
)
def test_parts_should_be_sorted_when_they_are_not_equal(
    value: int,
    num_parts: int
) -> None:
    assert sorted(split_integer(
        value, num_parts)) == split_integer(value, num_parts)


@pytest.mark.parametrize(
    "value, num_parts", [
        (5, 10),
        (2, 8),
        (4, 3)
    ]
)
def test_should_add_zeros_when_value_is_less_than_number_of_parts(
    value: int,
    num_parts: int
) -> None:
    assert len(split_integer(value, num_parts)) == num_parts
