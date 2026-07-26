from app.split_integer import split_integer
import pytest


@pytest.mark.parametrize(
    "value, number_of_parts, sum_of_parts",
    [
        (8, 2, [4, 4]),
        (11, 3, [3, 4, 4])
    ],
    ids=[
        "value: 8, number_of_parts: 2",
        "value: 11, number_of_parts: 3"
    ]
)
def test_sum_of_the_parts_should_be_equal_to_value(
    value: int,
    number_of_parts: int,
    sum_of_parts: list[int]
) -> None:
    assert (
        (
            sum(split_integer(value, number_of_parts)) == sum(sum_of_parts)
            and (
                split_integer(value, number_of_parts)[-1]
                - split_integer(value, number_of_parts)[0]
                <= 1
            )
        )
    ), f"Sum of all parts should be equal to {value}"


@pytest.mark.parametrize(
    "value, number_of_parts, equal_part",
    [
        (6, 2, [3, 3]),
        (16, 4, [4, 4, 4, 4])
    ],
    ids=[
        "value: 6, number_of_parts: 2",
        "value: 16, number_of_parts: 4"
    ]
)
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
    value: int,
    number_of_parts: int,
    equal_part: list[int]
) -> None:
    assert (
        split_integer(value, number_of_parts) == equal_part
    ), (
        "List should consist only out of equal values, ",
        f"each value should be: {equal_part[0]}"
    )


@pytest.mark.parametrize(
    "value, number_of_parts, expected_value",
    [
        (8, 1, [8]),
        (22, 1, [22])
    ],
    ids=[
        "value: 8, number_of_parts: 1",
        "value: 22, number_of_parts: 1"
    ]
)
def test_should_return_part_equals_to_value_when_split_into_one_part(
    value: int,
    number_of_parts: int,
    expected_value: list[int]
) -> None:
    assert (
        split_integer(value, number_of_parts) == expected_value
    ), "Returned part should be always equal to value when divided by 1"


@pytest.mark.parametrize(
    "value, number_of_parts, expected_parts",
    [
        (9, 4, [2, 2, 2, 3]),
        (32, 6, [5, 5, 5, 5, 6, 6])
    ],
    ids=[
        "value: 9, number_of_parts: 4",
        "value: 32, number_of_parts: 6"
    ]
)
def test_parts_should_be_sorted_when_they_are_not_equal(
    value: int,
    number_of_parts: int,
    expected_parts: list[int]
) -> None:
    assert (
        split_integer(value, number_of_parts) == expected_parts
    ), "Parts should be sorted!"


@pytest.mark.parametrize(
    "value, number_of_parts, parts_with_zeros",
    [
        (1, 5, [0, 0, 0, 0, 1]),
        (2, 4, [0, 0, 1, 1])
    ],
    ids=[
        "value: 1, number_of_parts: 5",
        "value: 2, number_of_parts: 4"
    ]
)
def test_should_add_zeros_when_value_is_less_than_number_of_parts(
    value: int,
    number_of_parts: int,
    parts_with_zeros: list[int]
) -> None:
    assert (
        split_integer(value, number_of_parts) == parts_with_zeros
    ), (
        "When 'number_of_parts' is bigger than 'value', ",
        "parts list should contain zeros"
    )
