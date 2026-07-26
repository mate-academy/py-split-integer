import pytest

from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        (8, 1),
        (6, 2),
        (17, 6),
        (32, 6)
    ]
)
def test_sum_of_the_parts_should_be_equal_to_value(
    value: int,
    number_of_parts: int
) -> None:
    assert (
        sum(split_integer(value, number_of_parts)) == value
    ), (f"Failed: result sum with {value} with {number_of_parts} "
        f"not equal to {value}")


@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        (2, 2),
        (4, 2),
        (32, 8),
        (32, 16),
        (32, 32)
    ]
)
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
    value: int,
    number_of_parts: int
) -> None:
    assert (
        len(set(split_integer(value, number_of_parts))) == 1
    ), (f"Did not split into equal parts for value {value} "
        f"and number of parts {number_of_parts}")


@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        (2, 1),
        (9999916, 1),
        (17, 1)
    ]
)
def test_should_return_part_equals_to_value_when_split_into_one_part(
    value: int,
    number_of_parts: int
) -> None:
    assert (
        split_integer(value, number_of_parts)[0] == value
    ), f"Part not equal to value {value} when split into one part"


@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        (8, 1),
        (6, 7),
        (17, 4),
        (53, 51)
    ]
)
def test_parts_should_be_sorted_when_they_are_not_equal(
    value: int,
    number_of_parts: int
) -> None:
    result = split_integer(value, number_of_parts)
    assert (
        result == sorted(result)
    ), (f"Parts not sorted for value {value} and "
        f"number of parts {number_of_parts}")


@pytest.mark.parametrize(
    "value,number_of_parts,result",
    [
        (5, 10, [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]),
        (6, 7, [0, 1, 1, 1, 1, 1, 1]),
        (1, 7, [0, 0, 0, 0, 0, 0, 1])
    ]
)
def test_should_add_zeros_when_value_is_less_than_number_of_parts(
    value: int,
    number_of_parts: int,
    result: list[int]
) -> None:
    assert (
        split_integer(value, number_of_parts) == result
    ), (f"No zeros found in test with value {value} and "
        f"number of parts {number_of_parts}")


@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        (8, 1),
        (6, 2),
        (17, 6),
        (32, 6)
    ]
)
def test_difference_between_min_and_max_is_one(
    value: int,
    number_of_parts: int
) -> None:
    result = split_integer(value, number_of_parts)
    assert (
        max(result) - min(result) <= 1
    ), (f"Failed: min and max greater than 1 with {value} with "
        f"{number_of_parts} not equal to {value}")


@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        (8, 1),
        (6, 2),
        (17, 6),
        (1023, 7)
    ]
)
def test_num_parts_returned_is_correct(
    value: int,
    number_of_parts: int
) -> None:
    assert (
        len(split_integer(value, number_of_parts)) == number_of_parts
    ), (f"Failed: number of elements returned not correct with "
        f"{value} with {number_of_parts} not equal to {value}")
