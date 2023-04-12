import pytest

from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (8, 1),
        (6, 2),
        (17, 4)
    ]
)
def test_sum_of_the_parts_should_be_equal_to_value(
        value: int,
        number_of_parts: int
) -> None:
    assert (
        sum(split_integer(value, number_of_parts)) == value
    ), (f"Sum {split_integer(value, number_of_parts)} should "
        f"be equal to {value}")


@pytest.mark.parametrize(
    "value, parts",
    [
        (4, 2),
        (56, 8),
        (64, 10)
    ]
)
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
        value: int,
        parts: int
) -> None:
    assert (
        len(split_integer(value, parts)) == parts
    ), (
        f"Length of list should be equal to {parts}, "
        f"when it`s equal to {len(split_integer(value, parts))}"
    )


@pytest.mark.parametrize(
    "value, parts",
    [
        (8, 1),
        (15673, 1),
        (0, 1)
    ]
)
def test_should_return_part_equals_to_value_when_split_into_one_part(
        value: int,
        parts: int
) -> None:
    assert (
        len(split_integer(value, parts)) == parts
    ), (
        f"Function should return 1 element, "
        f"when returns {split_integer(value, parts)}"
    )


@pytest.mark.parametrize(
    "value, parts, result",
    [
        (6, 2, [3, 3]),
        (17, 4, [4, 4, 4, 5]),
        (37, 7, [5, 5, 5, 5, 5, 6, 6])
    ]
)
def test_parts_should_be_sorted_when_they_are_not_equal(
        value: int,
        parts: int,
        result: list
) -> None:
    assert (
        split_integer(value, parts) == result
    ), "Function should return sorted list in descending order"


@pytest.mark.parametrize(
    "value, parts, result",
    [
        (3, 4, [0, 1, 1, 1]),
    ]
)
def test_should_add_zeros_when_value_is_less_than_number_of_parts(
        value: int,
        parts: int,
        result: list
) -> None:
    assert (
        result == split_integer(value, parts)
    ), (
        f"Should return {result}, when number_of_parts > value"
        f"({parts} > {value})"
    )
