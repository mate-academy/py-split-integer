import pytest
from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (8, 1),
        (6, 2),
        (17, 4),
        (32, 6)
    ]
)
def test_sum_of_the_parts_should_be_equal_to_value(
        value: int,
        number_of_parts: int,
) -> None:
    assert (
        sum(split_integer(value, number_of_parts)) == value
    ), "Sum of parts not equal to value"


@pytest.mark.parametrize(
    "value, num_of_parts",
    [
        (6, 2),
        (27, 3),
        (50, 5)
    ]
)
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
        value: int,
        num_of_parts: int
) -> None:
    assert (
        len(set(split_integer(value, num_of_parts))) == 1
    ), "Result should contain equal parts"


@pytest.mark.parametrize(
    "value, num_of_parts",
    [
        (8, 1),
        (1, 1),
        (100, 1)
    ]
)
def test_should_return_part_equals_to_value_when_split_into_one_part(
        value: int,
        num_of_parts: int
) -> None:
    assert (
        split_integer(value, num_of_parts) == [value]
    ), "Result should be equal to value"


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (17, 4),
        (32, 6),
        (46, 9)
    ]
)
def test_parts_should_be_sorted_when_they_are_not_equal(
        value: int,
        number_of_parts: int
) -> None:
    result = split_integer(value, number_of_parts)
    assert (
        result == sorted(result)
    ), "Result is not sorted"


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (1, 2),
        (1, 3),
        (10, 20)
    ]
)
def test_should_add_zeros_when_value_is_less_than_number_of_parts(
        value: int,
        number_of_parts: int
) -> None:
    result = split_integer(value, number_of_parts)
    assert (
        result.count(0) == number_of_parts - value
    ), "Function amount of zero is incorrect"
