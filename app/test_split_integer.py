from app.split_integer import split_integer
import pytest


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (6, 2),
        (36, 8),
        (24, 6)
    ]
)
def test_sum_of_the_parts_should_be_equal_to_value(value, number_of_parts) -> None:
    assert sum(split_integer(value, number_of_parts)) == value, "Sum of all elements should be equal to value"


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (16, 4),
        (15, 3)
    ]
)
def test_should_split_into_equal_parts_when_value_divisible_by_parts(value, number_of_parts) -> None:
    assert [value // number_of_parts] * number_of_parts == split_integer(value, number_of_parts), \
        "All elements should be equal"


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (8, 1),
        (7, 1)
    ]
)
def test_should_return_part_equals_to_value_when_split_into_one_part(value, number_of_parts) -> None:
    assert [value] == split_integer(value, number_of_parts), \
        "The only one element of list should be equal to value"


@pytest.mark.parametrize(
    "value, number_of_parts, result",
    [
        (17, 3, [5, 6, 6]),
        (19, 5, [3, 4, 4, 4, 4])
    ]
)
def test_parts_should_be_sorted_when_they_are_not_equal(value, number_of_parts, result) -> None:
    assert split_integer(value, number_of_parts) == result, "List should be sorted"


@pytest.mark.parametrize(
    "value, number_of_parts, result",
    [
        (2, 3, [0, 1, 1]),
        (6, 8, [0, 0, 1, 1, 1, 1, 1, 1])
    ]
)
def test_should_add_zeros_when_value_is_less_than_number_of_parts(value, number_of_parts, result) -> None:
    assert split_integer(value, number_of_parts) == result, \
        f"First {number_of_parts - value} elements should be zero"


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (17, 4),
        (32, 6),
        (20, 5)
    ]
)
def test_difference_between_parts_is_at_most_one(value, number_of_parts):
    result = split_integer(value, number_of_parts)
    assert max(result) - min(result) <= 1
