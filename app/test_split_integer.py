from app.split_integer import split_integer
import pytest


@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        (6, 2),
        (17, 4),
        (32, 6),
        (100, 9)
    ]
)
def test_sum_of_the_parts_should_be_equal_to_value(
    value: int,
    number_of_parts: int
) -> None:
    assert (
        sum(split_integer(value, number_of_parts)) == value
    )


@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        (6, 2),
        (15, 3),
        (32, 4),
        (100, 5)
    ]
)
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
    value: int,
    number_of_parts: int
) -> None:
    assert (
        all(split_integer(value, number_of_parts)[0] == num
            for num in split_integer(value, number_of_parts))
    )


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert (
        split_integer(10, 1) == [10]
    )


@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        (8, 7),
        (6, 4),
        (32, 9),
        (11, 16)
    ]
)
def test_parts_should_be_sorted_when_they_are_not_equal(
    value: int,
    number_of_parts: int
) -> None:
    result = split_integer(value, number_of_parts)
    assert result == sorted(result)


@pytest.mark.parametrize(
    "value,number_of_parts,result",
    [
        (1, 5, [0, 0, 0, 0, 1]),
        (11, 16, [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),
        (4, 12, [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]),
    ]
)
def test_should_add_zeros_when_value_is_less_than_number_of_parts(
    value: int,
    number_of_parts: int,
    result: list
) -> None:
    assert (
        split_integer(value, number_of_parts) == result
    )


@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        (17, 4),
        (32, 6),
        (100, 9),
        (1, 5),
        (11, 16)
    ],
)
def test_should_return_exactly_number_of_parts_elements(
    value: int,
    number_of_parts: int
) -> None:
    assert len(split_integer(value, number_of_parts)) == number_of_parts


@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        (17, 4),
        (100, 9),
        (1, 5),
        (11, 16)
    ],
)
def test_difference_between_max_and_min_should_not_exceed_one(
    value: int,
    number_of_parts: int
) -> None:
    result = split_integer(value, number_of_parts)
    assert max(result) - min(result) <= 1
