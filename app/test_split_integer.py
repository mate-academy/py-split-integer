from app.split_integer import split_integer
import pytest


@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        (8, 1), (6, 2), (17, 4), (32, 6)
    ]
)
def test_sum_of_the_parts_should_be_equal_to_value(
        value: int, number_of_parts: int) -> None:
    assert (
        sum(split_integer(value, number_of_parts)) == value
    ), "Sum of the parts should be equal to value"


@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        (8, 1), (6, 2), (17, 4), (32, 6)
    ]
)
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
        value: int, number_of_parts: int) -> None:
    result = split_integer(value, number_of_parts)
    assert (
        max(result) - min(result) <= 1
    ), "Split not into equal parts when value divisible by parts"


@pytest.mark.parametrize(
    "value",
    [
        8, 6, 17, 32
    ]
)
def test_should_return_part_equals_to_value_when_split_into_one_part(
        value: int) -> None:
    assert (
        split_integer(value, 1) == [value]
    ), f"if {'number_of_parts'} equals to 1 should return {'value'}"


@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        (8, 1), (6, 2), (17, 4), (32, 6)
    ]
)
def test_parts_should_be_sorted_when_they_are_not_equal(
        value: int, number_of_parts: int) -> None:
    result = split_integer(value, number_of_parts)
    assert (
        result == sorted(result)
    ), "Parts should be sorted when they are not equal"


@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        (1, 8), (2, 6), (1, 17), (6, 32)
    ]
)
def test_should_add_zeros_when_value_is_less_than_number_of_parts(
        value: int, number_of_parts: int) -> None:
    result = split_integer(value, number_of_parts)
    assert (
        result == [0] * (number_of_parts - value) + [1] * value
    ), "Should add zeros"
