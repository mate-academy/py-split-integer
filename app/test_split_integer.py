from app.split_integer import split_integer
import pytest


@pytest.mark.parametrize(
    "value,number_of_parts,result",
    [
        (32, 6, [5, 5, 5, 5, 6, 6])
    ]
)
def test_sum_of_the_parts_should_be_equal_to_value(value: int,
                                                   number_of_parts: int,
                                                   result: list) -> None:
    parts = split_integer(value,
                          number_of_parts)

    assert (
        sum(parts) == value
    ), f"Sum of the {parts} should be equal to {value}"


@pytest.mark.parametrize(
    "value,number_of_parts,result",
    [
        (6, 2, [3, 3])
    ]

)
def test_should_split_into_equal_parts_when_value_divisible_by_parts(value: int,
                                                                     number_of_parts: int,
                                                                     result: list) -> None:
    parts = split_integer(value,
                          number_of_parts)

    assert (
        parts == result
    ), f"Should split into equal parts when {value} divisible by parts"


@pytest.mark.parametrize(
    "value,number_of_parts,result",
    [
        (6, 1, [6])
    ]

)
def test_should_return_part_equals_to_value_when_split_into_one_part(value: int,
                                                                     number_of_parts: int,
                                                                     result: list) -> None:
    parts = split_integer(value, number_of_parts)

    assert (
        parts[0] == value
    ), f"{parts[0]} must be equals to {value} when split into one part"


@pytest.mark.parametrize(
    "value,number_of_parts,result",
    [
        (32, 6, [5, 5, 5, 5, 6, 6])
    ]

)
def test_parts_should_be_sorted_when_they_are_not_equal(value: int,
                                                        number_of_parts: int,
                                                        result: list) -> None:
    parts = split_integer(value, number_of_parts)

    assert (
        parts == result
    ), f"{parts} should be sorted when they are not equal"


@pytest.mark.parametrize(
    "value,number_of_parts,result",
    [
        (5, 6, [0])
    ]

)
def test_should_add_zeros_when_value_is_less_than_number_of_parts(value: int,
                                                                  number_of_parts: int,
                                                                  result: list) -> None:
    parts = split_integer(value, number_of_parts)

    assert (
        parts[0] == 0
    )
