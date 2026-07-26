import pytest

from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value,parts",
    [
        (8, 1),
        (6, 2),
        (17, 4),
        (32, 6),
        (4, 5)
    ]
)
def test_sum_of_the_parts_should_be_equal_to_value(
    value: int,
    parts: int
) -> None:
    assert (
        sum(split_integer(value, parts)) == value
    ), f"Sum of the parts should be equal to {value}"


@pytest.mark.parametrize(
    "value,parts",
    [
        (8, 1),
        (6, 2),
        (17, 4),
        (32, 6),
        (4, 5)
    ]
)
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
    value: int,
    parts: int
) -> None:
    if value % parts == 0:
        assert (
            (max(split_integer(value, parts))
             - min(split_integer(value, parts)) <= 1)
        ), f"Should consist of {parts} equal parts"


@pytest.mark.parametrize(
    "value,parts",
    [
        (8, 1),
        (6, 2),
        (17, 4),
        (32, 6),
        (4, 5)
    ]
)
def test_should_return_part_equals_to_value_when_split_into_one_part(
    value: int,
    parts: int
) -> None:
    if parts == 1:
        assert (
            (len(split_integer(value, parts)) == 1
             and split_integer(value, parts)[0] == value)
        ), (f"Should consist of {parts} part equal to {value}")


@pytest.mark.parametrize(
    "value,parts",
    [
        (8, 1),
        (6, 2),
        (17, 4),
        (32, 6),
        (4, 5)
    ]
)
def test_parts_should_be_sorted_when_they_are_not_equal(
    value: int,
    parts: int
) -> None:
    if value % parts != 0:
        assert (
            sorted(split_integer(value, parts)) == split_integer(value, parts)
        ), "Result is not sorted"


@pytest.mark.parametrize(
    "value,parts",
    [
        (8, 1),
        (6, 2),
        (17, 4),
        (32, 6),
        (4, 5)
    ]
)
def test_should_add_zeros_when_value_is_less_than_number_of_parts(
    value: int,
    parts: int
) -> None:
    if value < parts :
        assert (
            split_integer(value, parts).count(0) == (parts - value)
        ), f"Should be have {parts - value} added"
