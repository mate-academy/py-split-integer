import pytest

from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        (7, 2),
        (32, 6),
        (0, 100),
        (10, 10)
    ]
)
def test_sum_of_the_parts_should_be_equal_to_value(
        value: int, number_of_parts: int) -> None:
    assert (
            sum(split_integer(value, number_of_parts)) == value
    ), (f"Function split_integer({value}, {number_of_parts}) "
        f"should return parts which sum will be equal to {value}")


@pytest.mark.parametrize(
    "value, number_of_parts, parts",
    [
        (2, 2, [1, 1]),
        (10, 2, [5, 5]),
        (36, 6, [6, 6, 6, 6, 6, 6]),
        (100, 4, [25, 25, 25, 25])
    ]
)
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
        value: int, number_of_parts: int, parts: list) -> None:
    assert (
            split_integer(value, number_of_parts) == parts
    ), (f"Function split_integer({value}, {number_of_parts}) "
        f"should return {parts}")


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (2, 1),
        (3456, 1),
        (0, 1)
    ]
)
def test_should_return_part_equals_to_value_when_split_into_one_part(
        value: int, number_of_parts: int) -> None:
    assert (
            split_integer(value, number_of_parts)[0] == value
    ), (f"Function split_integer({value}, {number_of_parts}) "
        f"should return parts which will be equal to {value}")


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (3, 2),
        (345, 4),
        (19, 5)
    ]
)
def test_parts_should_be_sorted_when_they_are_not_equal(
        value: int, number_of_parts: int) -> None:
    assert (
            split_integer(value, number_of_parts) == sorted(split_integer(value, number_of_parts))
    ), (f"Function split_integer should return "
        f"{sorted(split_integer(value, number_of_parts))}, "
        f"got {split_integer(value, number_of_parts)} instead")


@pytest.mark.parametrize(
    "value, number_of_parts, parts",
    [
        (3, 5, [0, 0, 1, 1, 1]),
        (1, 2, [0, 1]),
    ]
)
def test_should_add_zeros_when_value_is_less_than_number_of_parts(
        value: int, number_of_parts: int, parts: list) -> None:
    assert (
            split_integer(value, number_of_parts) == parts
    ), (f"Function split_integer should return "
        f"{parts}, got {split_integer(value, number_of_parts)} instead")
