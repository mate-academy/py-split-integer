import pytest

from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        (6, 2),
        (17, 4),
        (32, 6)
    ]
)
def test_sum_of_the_parts_should_be_equal_to_value(
        value: int, number_of_parts: int
) -> None:
    assert (
        sum(split_integer(value, number_of_parts)) == value
    ), "Sum of the parts should be equal to the value"


@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        (18, 3),
        (30, 6)
    ]
)
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
        value: int, number_of_parts: int
) -> None:
    assert (
        len(set(split_integer(value, number_of_parts))) == 1
    ), "Integer should be split into equal parts when value divisible by parts"


@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        (8, 1),
        (15, 1)
    ]
)
def test_should_return_part_equals_to_value_when_split_into_one_part(
        value: int, number_of_parts: int
) -> None:
    assert (
        split_integer(value, number_of_parts)[0] == value
    ), "Part should be equal to value when split into one part"


@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        (17, 4),
        (32, 6)
    ]
)
def test_parts_should_be_sorted_when_they_are_not_equal(
        value: int, number_of_parts: int
) -> None:
    result = split_integer(value, number_of_parts)
    assert (
        result == sorted(result)
    ), "Parts should be sorted when they are not equal"


@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        (5, 6),
        (7, 10)
    ]
)
def test_should_add_zeros_when_value_is_less_than_number_of_parts(
        value: int, number_of_parts: int
) -> None:
    assert (
        0 in split_integer(value, number_of_parts)
    ), "Should add zeros when value is less than number of parts"
