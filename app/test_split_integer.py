import pytest

from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        (9, 3)
    ]
)
def test_sum_of_the_parts_should_be_equal_to_value(
        value: int,
        number_of_parts: int
) -> None:
    assert sum(split_integer(value, number_of_parts)) == value, (
        "Sum of the parts should be equal to value"
    )


@pytest.mark.parametrize(
    "value,number_of_parts,result",
    [
        (12, 4, [3, 3, 3, 3])
    ]
)
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
        value: int,
        number_of_parts: int,
        result: int
) -> None:
    assert split_integer(value, number_of_parts) == result, (
        "Function should split into equal parts "
        "when value divisible by parts"
    )


@pytest.mark.parametrize(
    "value,number_of_parts,result",
    [
        (12, 1, [12])
    ]
)
def test_should_return_part_equals_to_value_when_split_into_one_part(
        value: int,
        number_of_parts: int,
        result: int
) -> None:
    assert split_integer(value, number_of_parts) == result, (
        "Function should return part equals to value when split into one part"
    )


@pytest.mark.parametrize(
    "value,number_of_parts,result",
    [
        (17, 4, [4, 4, 4, 5])
    ]
)
def test_parts_should_be_sorted_when_they_are_not_equal(
        value: int,
        number_of_parts: int,
        result: int
) -> None:
    assert split_integer(value, number_of_parts) == result, (
        "Parts should be sorted when they are not equal"
    )


@pytest.mark.parametrize(
    "value,number_of_parts,result",
    [
        (4, 6, [0, 0, 1, 1, 1, 1])
    ]
)
def test_should_add_zeros_when_value_is_less_than_number_of_parts(
        value: int,
        number_of_parts: int,
        result: int
) -> None:
    assert split_integer(value, number_of_parts) == result
