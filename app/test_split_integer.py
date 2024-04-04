import pytest

from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert (
        sum(split_integer(100, 3)) == 100
    ), "Sum of parts is not equal to the original value"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert (
        split_integer(100, 4).count(25) == 4
    ), "Value not split into equal parts"


@pytest.mark.parametrize(
    "value,number_of_parts,expected_result",
    [
        (10, 1, [10]),
        (10, 10, [1] * 10)
    ],
    ids=[
        "Split into one part with value 10",
        "Split into 10 equal parts with value 1"
    ]
)
def test_should_return_part_equals_to_value_when_split_into_one_part(
    value: int, number_of_parts: int, expected_result: list
) -> None:
    assert (
        split_integer(value, number_of_parts) == expected_result
    ), "Value not split into one part or into 10 equal parts"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert (
        split_integer(100, 3) == [33, 33, 34]
    ), "Parts are not sorted"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert (
        split_integer(3, 5) == [0, 0, 1, 1, 1]
    ), "Zeros not added when value is less than the number of parts"
