import pytest
from typing import List
from app.split_integer import split_integer


@pytest.mark.parametrize("value, parts, expected", [
    (8, 1, [8]),
    (15, 1, [15]),
    (8, 4, [2, 2, 2, 2]),
    (10, 5, [2, 2, 2, 2, 2]),
])
def test_split_integer(value: int, parts: int, expected: List[int]) -> None:
    assert split_integer(value, parts) == expected, (
        f"Expected {expected} when splitting {value} into {parts} parts"
    )


@pytest.mark.parametrize("value, parts, expected_sum", [
    (8, 1, 8),
    (8, 4, 8),
    (10, 5, 10),
    (17, 4, 17),
    (32, 6, 32),
])
def test_sum_of_the_parts_should_be_equal_to_value(
    value: int, parts: int, expected_sum: int
) -> None:
    assert sum(split_integer(value, parts)) == expected_sum, (
        f"Sum of the parts should be equal to the original value: "
        f"{expected_sum}"
    )


@pytest.mark.parametrize("value, parts, expected", [
    (17, 4, [4, 4, 4, 5]),
    (32, 6, [5, 5, 5, 5, 6, 6]),
])
def test_parts_should_be_sorted_when_they_are_not_equal(
    value: int, parts: int, expected: List[int]
) -> None:

    assert split_integer(
        value, parts
    ) == sorted(split_integer(value, parts)), "Parts should be sorted"
    assert split_integer(
        value, parts
    ) == expected, f"Expected sorted parts to be {split_integer(value, parts)}"


@pytest.mark.parametrize("value, parts, expected", [
    (3, 5, [0, 0, 1, 1, 1]),
])
def test_should_add_zeros_when_value_is_less_than_number_of_parts(
    value: int, parts: int, expected: List[int]
) -> None:
    assert split_integer(value, parts) == expected, (
        "When value is less than the number of parts, "
        "the result should include zeros."
    )
