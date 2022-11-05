import pytest

from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        (8, 1),
        (6, 2),
        (17, 4),
        (32, 6)
    ]
)
def test_sum_of_the_parts_should_be_equal_to_value(
        value: int,
        number_of_parts: int
) -> None:
    parts = split_integer(value, number_of_parts)
    assert (sum(parts) == value),\
        f"Sum of the {parts} should be equal to {value}"


@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        (108, 12),
        (30, 3),
        (66, 6),
        (36, 4)
    ]
)
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
        value: int,
        number_of_parts: int
) -> None:
    parts = split_integer(value, number_of_parts)
    assert (parts.count(parts[0]) == len(parts)),\
        "all of the parts should be equal when value divisible by parts"


@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        (108, 1),
        (1, 1),
        (20, 1),
    ]
)
def test_should_return_part_equals_to_value_when_split_into_one_part(
        value: int,
        number_of_parts: int
) -> None:
    assert (split_integer(value, number_of_parts)[0] == value),\
        "When value split into one part, return value should be equal to value"


@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        (58, 4),
        (83, 10),
        (21, 15),
    ]
)
def test_parts_should_be_sorted_when_they_are_not_equal(
        value: int,
        number_of_parts: int
) -> None:
    parts = split_integer(value, number_of_parts)
    assert (sorted(
        parts) == parts), "Parts should be sorted when they are not equal"


@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        (12, 14),
        (9, 11),
        (10, 15),
    ]
)
def test_should_add_zeros_when_value_is_less_than_number_of_parts(
        value: int, number_of_parts: int
) -> None:
    assert (split_integer(value, number_of_parts).count(
        0) > 0), "Should add zeros when value is less than number of parts"
